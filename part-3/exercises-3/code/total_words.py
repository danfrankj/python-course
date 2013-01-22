def num_words(file_name):
    with open(file_name, 'r') as f:
        total = 0
        for line in f:
           total += len(line.split())
        return total
    
print num_words('course_description.txt')
