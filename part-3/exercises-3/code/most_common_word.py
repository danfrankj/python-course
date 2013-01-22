def most_common(file_name):
    with open(file_name, 'r') as f:
        words = {}
        for line in f:
           line_words = line.split()
           for word in line_words:
               if word in words:
                   words[word] += 1
               else:
                   words[word] = 1
        
        return sorted(words.items(),
                      key=lambda x: x[1],
                      reverse=True)[0]

print most_common('bill_of_rights.txt')
