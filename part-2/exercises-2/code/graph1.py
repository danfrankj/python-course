graph = {'A': ['B', 'F'],
         'B': ['C'],
         'C': ['B'],
         'D': [],
         'E': ['D'],
         'F': []}

def add_edge(i, j):
    graph[i] += [j]

add_edge('F', 'B')

