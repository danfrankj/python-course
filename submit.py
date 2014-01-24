#!/usr/bin/env python

# CS107 Submit Script
# Shamelessly stolen by dlwh for Linguist180 1/2009
# Authors: Justin Haugh and Abhishek Bajoria (and Susan Shepard)
# First written: 04/12/2003
#
# Key other setup:
# -create the submissions and submit_files directories before anyone
#  submits so that permissions will be inherited correctly
# -/usr/class/cs107/submissions must be created with system:anyuser li
# -/usr/class/cs107/bin/submit_files must be created with system:anyuser
#                                    rliwk
# -/usr/class/cs107/bin should be system:anyuser rl
# -requires
#           /usr/class/bin/assign_deadlines.txt with assignment deadline
#           info.  last line must have a RETURN or list of assignments
#           won't print out correctly!!!  Format is:
#           hwNum DueDate DueDateTime compile(yes|no) hwName inGroups(yes|no) filesToSubmit1,filesToSubmit2,filesToSubmit3,...
#      (no whitespace in the list of filesToSubmit)
#
#           /usr/class/bin/submit_files/TA_list.txt with names of TAs
#
# Updates:
# 04/20/2003 -- added assignment listing
# 09/29/2003 -- user chooses assignment now and submits from current
#               directory only.  Same student-ta for each assignment
#               shepard8 (Susan Shepard)
# 10/20/2003 -- modified to prompt user for a submit directory. Presents
#               a list of files that will be copied.  Loops until the
#               user accepts a list.  Will not allow a submission of
#               no files or an invalid directory
# 10/21/2003 -- modified to accept different assign_deadlines.txt format
#               hwNum DueDate DueDateTime compile(yes|no) hwName
#               whether compile occurs or not is now dependent on the assignment

import sys
import shutil
import pwd
import os
import time
import math
import string
import importlib
from subprocess import call
import webbrowser
import random


# Global Constants
COURSE_NAME = "cme193"
#HOME_DIR = "/afs/ir.stanford.edu/class/cme193/"
HOME_DIR = "/afs/ir.stanford.edu/users/d/a/danfrank/cme193/"
#HOME_DIR = "/home/danfrank/cme193/"
SUBMIT_CONFIG_DIR = HOME_DIR + "/config/"  # system:anyuser rl
SUBMIT_DIR = HOME_DIR + "/submissions/"  # system:anyuser iw
GRADER_DIR = HOME_DIR + "/graders/"
ASSIGN_DEADLINES = SUBMIT_CONFIG_DIR + "/assign_deadlines.txt"

HOMEWORK = None
HOMEWORK_STRING = None
DUE_DATE = None
MAX_LATE_DAYS = 3

#-----------------------------------------------------------------
# subfunctions
#-----------------------------------------------------------------


#-----------------------------------------------------------------
# GetAssignmentInfo
#
# Get assignment record based on user input.
# If record exists in due dates file, return it.
# Otherwise, print error and quit.
#-----------------------------------------------------------------
def GetAssignmentInfo():

  # Find out which assignments can be turned in...
    dueDateFile = None

    try:
        dueDateFile = open(ASSIGN_DEADLINES, "r")
        dueDateMappings = dueDateFile.read().splitlines()

    except IOError, e:
        print "ERROR reading the due date file: ", e
        print "Please contact the " + COURSE_NAME + " staff immediately, and include the output of this script."
        sys.exit()

    dueDateFile.close()
    dueDateMappings.sort()
    print "****************************************************************\n"
    print "Which project are you submitting? "

    hwNums = [int(string.split(mapping, None, 7)[0]) for mapping in dueDateMappings]
    for mapping in dueDateMappings:
        # each line contains: "hw# DueDate DueDateTime compile(yes|no) hwName filesToSubmit
        dueDateSplitted = string.split(mapping, None, 7)
        if not dueDateSplitted:
            continue

        hwNum = dueDateSplitted[0]
        hwName = dueDateSplitted[4]
        print "  %s) %s" % (hwNum, hwName)

    ans = raw_input("\nEnter the assignment number (0, 1 ...; -1 to quit): ")
    # Handle raw input
    ans = int(ans)
    if ans == -1:
        print "Exiting..."
        sys.exit()

    if not ans in hwNums:
        # if we get here, no matching assignment was found for input
        print "ERROR: No matching assignment found for ", ans,  "."
        print "Exiting...\n"
        sys.exit()
    else:
        splitted = string.split(dueDateMappings[ans], None, 7)
        print "You are submitting %s (%s)" % (splitted[0], splitted[4])
        return splitted
# end of GetAssignmentInfo()


#-----------------------------------------------------------------
# getSourceDirectory();
#
# prompts the user to enter a path.  Loops until she enters a
# valid path.  Return the path and the list of files to copy as
# a tuple. Checks that the path exists and is a valid dir and then
# creates a list of matching files
#-----------------------------------------------------------------
def getSourceDirectory(filesToSubmit):
    # Get a regular expression pattern matcher to match files to copy
    #pattern = re.compile(r'\A[\w\-_]+\.(c|cc|cpp|h|java|scm|py)\Z|\AREADME\Z|\AMakefile\Z', re.IGNORECASE)

    # get the names of the files to submit
    filesToSubmit_names = string.split(string.strip(filesToSubmit), ",")

    print "****************************************************************\n"
    while 1:
        src = raw_input("Enter the path containing your submission files (press ENTER to use current directory): ")
        if src == '':
            src = '.'
        # if src begins with a ~, need to translate first.  expanduser is
        # no-op if src doesn't begin with a tilde
        src = os.path.expanduser(src)
        temp_path = os.path.abspath(src)  # translate to absolute

        if os.path.exists(temp_path) and os.path.isdir(temp_path):
            print "\nThe following files will be copied from %s:" % temp_path
            filesToCopy = []
            filesNotFound = []
            files = os.listdir(temp_path)
            # look for the files you want
            for filename in filesToSubmit_names:
                found = False
                for file in files:
                    if file == filename:
                        filesToCopy.append(file)
                        found = True
                if not found:
                    filesNotFound.append(filename)
            if len(filesNotFound) > 0:
                print "Files not found in this directory : ", filesNotFound, ". Please try again."
            else:
                for file in filesToCopy:
                    print "  " + file
                ans = raw_input("\nIs this correct (yes/no)?  (Enter 'no' to choose another source directory.) ")
                if ans in ('y', 'yes'):
                    return temp_path, filesToCopy  # user is satisfied, return the result
        else:
            # either source path doesn't exit or isn't a directory
            print temp_path, " is not a valid directory.  Please try again."
#end getSourceDirectory()


#-----------------------------------------------------------------
# Main (global) function
#-----------------------------------------------------------------

# Record the time of submission
# NOTE: this is off by an hour during DST, so you need to do the
# conversion found later (search for submitTimeString) before using
# it.

def main():
    SUBMIT_TIME = time.time()

    # Greeting message
    print "\n------------- Welcome to the " + COURSE_NAME + " Submit Script -------------\n"
    print "If you are using this script on a machine other than corn,"
    #print "epic, myth, fable, saga, or tree, please hit CTRL-C to cancel"
    print "please hit CTRL-C to cancel"
    print "this script, log into one of those machines and try again.\n"

    #------------------------------------
    # Get some relevant shell variables: student name, Leland ID, etc.
    USERID = os.environ['USER']
    STUDENT_NAME = pwd.getpwnam(USERID)[4]
    #HOST = os.environ['HOSTNAME']
	
    # Identity check
    print "\nYou are submitting for " + STUDENT_NAME  # + " from " + HOST
    print "If you're not " + STUDENT_NAME + ", then log out and try again"
    print "after logging into your own account.\n"


    #------------------------------------
    # determine assignment for submission
    assignment = GetAssignmentInfo()

    hwNum = assignment[0]
    dueDatePartOne = assignment[1]
    dueDatePartTwo = assignment[2]
    testCompile = assignment[3]
    hwName = assignment[4]
    inGroups = assignment[5]
    filesToSubmit = assignment[6]
    grader = assignment[7]

    dueDate = dueDatePartOne + " " + dueDatePartTwo
    dueTime = time.strptime(dueDate, "%Y-%m-%d %H:%M:%S")

    #calculate which assignments are acceptable...
    # this is totally dumb but if you don't make the submit time
    # into a string and then back to seconds, it's off by an hour.
    # I'm sure it's a daylight savings time issue, but I can't
    # get localtime() or time() to do the right thing.
    submitTimeString = time.asctime(time.localtime(SUBMIT_TIME))
    SUBMIT_TIME = time.mktime(time.strptime(submitTimeString, "%a %b %d %H:%M:%S %Y"))

    diff = SUBMIT_TIME - time.mktime(dueTime)
    #daysDiff = math.ceil(diff/(3600*24))

    # Check that the user can actually still submit for the chosen assignment
    # if (daysDiff > MAX_LATE_DAYS):
    #  print "You have exceeded the max late days allowed on this assignment"
    #  print "(14).  Please contact %s staff if you believe this is a" % COURSE_NAME
    #  print "mistake. Exiting...\n"
    #  sys.exit();

    if diff < 0:
        lateDays = 0
    else:
        lateDays = math.ceil(diff / (3600 * 24))

    HOMEWORK = hwNum
    HOMEWORK_STRING = "Project " + hwNum + ": " + hwName

    # clever python: getSourceDirectory returns a tuple of the path and files
    # to copy list.  I can put two var names on lhs and tuple will be
    # appropriately unpacked. woo!
    to_submit_path, files_to_copy = getSourceDirectory(filesToSubmit)
    # First, we create their submit directory

    # Make the homework directory if it doesn't exist
    HWdir = SUBMIT_DIR + "/" + HOMEWORK
    if not os.path.exists(HWdir):
        try:
            os.mkdir(HWdir)
        except IOError, e:
            print "ERROR creating the " + HOMEWORK + " submission directory: " + HWdir
            print e
            print "Please contact the " + COURSE_NAME + " staff immediately, and include the output of this script."
            sys.exit()

    # Create the user's submit directory
    i = 0
    destDir = None
    MAX_SUBMISSIONS = 100
    while i < MAX_SUBMISSIONS:
        i = i + 1
        destDir = HWdir + "/" + USERID + "-" + str(i)
        if (not os.path.exists(destDir) and not os.path.exists(destDir + '-late')):
            if lateDays > MAX_LATE_DAYS:
                os.mkdir(destDir + '-late')
            else:
                os.mkdir(destDir)
            break
    if i == MAX_SUBMISSIONS:
	print "You have reached the maximum submissions for this assignment. Please contact course staff"
	sys.exit()

    if lateDays > MAX_LATE_DAYS:
        destDir = destDir + '-late'
    os.system('fs sa ' + destDir + ' ' + USERID + 'rildwa')
    # Copy their files
    print "****************************************************************\n"
    print "Copying files...\n"

    # Copy source files to their submit directory
    for file in files_to_copy:
        try:
            print "Copying file: " + file
            absoluteFileName = to_submit_path + "/" + file
            if os.path.isfile(absoluteFileName):
                if os.stat(absoluteFileName).st_size > 20 * 1024 * 1024:
                    print "ERROR: File must be less than 20MB"
                    sys.exit()
                shutil.copy(absoluteFileName, destDir + "/" + file)
            elif os.path.isdir(absoluteFileName):
                shutil.copytree(absoluteFileName, destDir + "/" + file)
            else:
                # I hate AFS
                in_file = open(absoluteFileName, 'r')
                out_file = open(destDir + "/" + file, 'w')
                out_file.write(in_file.read())
                out_file.flush()
                out_file.close()
        except IOError, e:
            print "ERROR during copying: ", e
            print "Please contact the " + COURSE_NAME + " staff immediately, and include the output of this script."
            sys.exit()

    # Create the GRADING file
    gradeFile = open(destDir + "/GRADING", 'w')
    gradeFile.write(USERID + "@stanford.edu" + "\n")
    gradeFile.write(STUDENT_NAME + "\n\n")
    gradeFile.write(HOMEWORK_STRING + "\n")
    gradeFile.write("Due date: " + dueDate + "\n")
    gradeFile.write("Submitted at: " + submitTimeString + "\n")
    gradeFile.write("Late days used: %d\n\n" % lateDays)

    # Run the grader
    print ''
    print "****************************************************************\n"
    print 'Running grader...'
    try:
        sys.path.append(GRADER_DIR)
        grader = os.path.splitext(os.path.basename(grader))[0]
        gr_lib = importlib.import_module(grader)
        score, pf = gr_lib.grade(destDir)
    except Exception as e:
        print "ERROR during grading", e
        print "Please make sure you are able to import your hw source files and correct any errors printed above"
        print "If you believe this is an error with the grader please contact the " + COURSE_NAME + " staff immediately, and include the output of this script."
        sys.exit()
    print "Grader successful. You may submit again up to the deadline, and the most recent grade will be used"
    print 'Score: ' + str(score) + ' Pass/Fail: ' + str(pf)
    gradeFile.write("Grade: %d \n" % score)
    gradeFile.write("PF: %s \n" % pf)
    gradeFile.write("Comments: \n\n")
    gradeFile.close()
    #cmd = GRADER_DIR + '/' + grader + ' ' + destDir
    #grader_retval = os.system(cmd)

    # Print "SUCCESS" message
    print "\n****************************************************************\n"
    print "SUCCESS! " + STUDENT_NAME + " submitted " + HOMEWORK_STRING
    print "at " + submitTimeString + ".  You used %d late days for this assignment." % lateDays

    if lateDays > MAX_LATE_DAYS:
        print "\nYou have exceeded the max late days on this assignment (" + str(MAX_LATE_DAYS) + '). Your submission will'
        print "not be graded unless you have permission from the staff for late submission."

    print ""
    print "The contents of your submission directory are:"
    call(['ls', '-l', destDir])

    print "\n\nAll done!  Thanks a lot!"

if __name__ == "__main__":
    sys.exit(main())
