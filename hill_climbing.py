import math

def add_edge(graph,node1,node2):
    if node1 in graph and node2 in graph:
        graph[node1].append(node2)
        graph[node2].append(node1)

def hillclimb(start,goal,graph):
    current=start
    print(graph)
    while True:
        if current==goal:
            return True
        
        neighbours=graph[current]

        next_val=max(neighbours,key=heuristic_values.get)


        if heuristic_values[next_val]<=heuristic_values[current]:
            break

        current=next_val

    return current==goal




nodes = ['A', 'B', 'C', 'D', 'E']
heuristic_values = {
    'E': 2,
    'D': 4,
    'C': 6,
    'B': 7,
    'A': 8
}
goal_state = 'A'



graph={node:[] for node in nodes}


print(graph)


add_edge(graph,'A','B')
add_edge(graph,'B','C')
add_edge(graph,'C','D')
add_edge(graph,'D','E')




reachable=hillclimb('E',goal_state,graph)

if reachable:
    print(f"the goal node {goal_state} is reachable")
else:
    print(f"the goal node {goal_state} is not reachable")