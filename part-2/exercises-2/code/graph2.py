# Assume the following edge weights:
# (A, B): 3; (A, F): 10
# (B, C): -4
# (C, B): 7
# (E, D): 8

graph = {'A': [('B', 3), ('F', 10)],
         'B': [('C', -4)],
         'C': [('B', 7)],
         'D': [],
         'E': [('D', 8)],
         'F': []}

def add_edge(i, j, weight):
    graph[i] += [(j, weight)]

# Assume (F, B) has weight -1
add_edge('F', 'B', -1)
