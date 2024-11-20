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

def bfs(start,graph):

    visited=set()
    queue=[start]
    visited.add(start)
    while queue:
        curr=queue.pop(0)
        print(curr,end='->')
        for neigh in graph[curr]:
            if neigh not in visited:
                queue.append(neigh)
                visited.add(neigh)



start=input("enter the start node:")
# goal=int(input("enter the goal node:"))

bfs(start,graph)

