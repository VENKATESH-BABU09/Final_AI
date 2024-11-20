graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': ['G', 'H'],
    'G': [],
    'H': []
}

def dfs(start,graph,visited=None):
    if visited is None:
        visited=set()
    visited.add(start)
    print(start,end='->')


    for neigh in graph[start]:
        if neigh not in visited:
            dfs(neigh,graph,visited)
    



start=input("enter the start node:")

dfs(start,graph)