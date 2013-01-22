def avg_upvotes(file_name):
    with open(file_name, 'r') as f:
        imgur_total = 0
        imgur_count = 0
        other_total = 0
        other_count = 0
        for line in f:
           data = line.split('|')
           if data[0].find('imgur') != -1:
               imgur_total += int(data[1])
               imgur_count += 1
           else:
               other_total += int(data[1])
               other_count += 1
        return (float(imgur_total) / imgur_count,
                float(other_total) / other_count)

print avg_upvotes('reddit_data.txt')
