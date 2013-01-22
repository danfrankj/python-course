def avg_comments(file_name):
    with open(file_name, 'r') as f:
        total = 0
        count = 0
        for line in f:
           total += int(line.split('|')[-1])
           count += 1
        return float(total) / count

print avg_comments('reddit_data.txt')
