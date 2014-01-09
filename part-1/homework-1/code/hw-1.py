
### arithmetic section
def arith1(x):
  """ Given an integer number x, returns:
      0, if x is negative or 0
      x, if x is strictly positve and less than or equal to 10
      10, otherwise """

  if x <= 0:
    return 0
  elif x <= 10:
    return x

  return 10

def arith2(x, y):
  """ Given two integer numbers x and y, returns:

      2x + y, if x is strictly greater than y
      4y - 3, if y is strictly greater than x
      x^3 + xy, if x is equal to y """

  return 0

def arith3(x, y, z):
  """ Given three integer numbers x, y, and z, returns:

      0, if any of the two numbers are the same
      1, if the numbers are ordered such that x < y and y < z
      2, otherwise """

  return 0

def arith4(x, y, z, w):
  """ Given four integer numbers x, y, z, and w, returns:

      the maximum of arith2(x, y) and arith2(z, w), if x is strictly less than y
      the sum of arith3(z, y, x) and arith1(w), otherwise """


  return 0


### string section
def str1(a):
  """ Given a string a, returns the string aaa """
  return a * 3

def str2(a, b):
  """ Given strings a and b, returns the string abbba """

  return ''

def str3(a, b, c):
  """ Given strings a, b, and c, returns the string abcabc """

  return ''

def str4(a, b, c, d):
  """ Given strings a, b, c, and d, returns:
      ab, if c and d are of the same length
      bbcc, otherwise   """

  return ''

### math section
def seq_add(start, end, k):
  """ Returns the sum of every k-th number between start and end. For example:
      seq_add(1, 10, 3) returns 1 + 4 + 7 + 10 = 22
      seq_add(1, 11, 3) returns 1 + 4 + 7 + 10 = 22
      seq_add(1, 5, 6) returns 1
      seq_add(4, 9, 2) returns 4 + 6 + 8 = 18
      seq_add(7, 7, 3) returns 7
      seq_add(-4, 8, 5) returns -4 + 1 + 6 = 3

      You can assume start <= end and that k > 0 """

  return 0

def fact(n):
  """ Returns n!, the factorial of n.  If n <= 0, return 0.  For example:
      fact(5) returns 5 * 4 * 3 * 2 * 1 = 120
      fact(-2) returns 0

      You can assume that n is an integer.

      You are not allowed to use Python's math library.  """

  return 0
