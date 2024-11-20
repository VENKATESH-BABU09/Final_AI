import heapq


def astar(graph,heuristics,start,goal):
    pq=[]
    heapq.heappush(pq,(0,start,[start]))

    costs={start:0}


    while pq:

        current_cost,current_node,path=heapq.heappop(pq)

        if current_node==goal:
            return path,current_cost
        
        for neigh,cost in graph[current_node].items():
            new_cost=costs[current_node]+cost
            if neigh not in costs or costs[neigh]>new_cost:
                costs[neigh]=new_cost
                total_cost=new_cost+heuristics[neigh]
                heapq.heappush(pq,(total_cost,neigh,path+[neigh]))

    return None,float("inf")
        

# graph = {
#     "Arad": [("Zerind", 75), ("Timisoara", 118), ("Sibiu", 140)],
#     "Zerind": [("Arad", 75), ("Oradea", 71)],
#     "Oradea": [("Zerind", 71), ("Sibiu", 151)],
#     "Timisoara": [("Arad", 118), ("Lugoj", 111)],
#     "Lugoj": [("Timisoara", 111), ("Mehadia", 70)],
#     "Mehadia": [("Lugoj", 70), ("Dobreta", 75)],
#     "Dobreta": [("Mehadia", 75), ("Craiova", 120)],
#     "Craiova": [("Dobreta", 120), ("Rimnicu Vilcea", 146), ("Pitesti", 138)],
#     "Sibiu": [("Arad", 140), ("Oradea", 151), ("Fagaras", 99), ("Rimnicu Vilcea", 80)],
#     "Rimnicu Vilcea": [("Sibiu", 80), ("Craiova", 146), ("Pitesti", 97)],
#     "Fagaras": [("Sibiu", 99), ("Bucharest", 211)],
#     "Pitesti": [("Rimnicu Vilcea", 97), ("Craiova", 138), ("Bucharest", 101)],
#     "Bucharest": [("Fagaras", 211), ("Pitesti", 101), ("Giurgiu", 90), ("Urziceni", 85)],
#     "Giurgiu": [("Bucharest", 90)],
#     "Urziceni": [("Bucharest", 85), ("Hirsova", 98), ("Vaslui", 142)],
#     "Hirsova": [("Urziceni", 98), ("Eforie", 86)],
#     "Eforie": [("Hirsova", 86)],
#     "Vaslui": [("Urziceni", 142), ("Iasi", 92)],
#     "Iasi": [("Vaslui", 92), ("Neamt", 87)],
#     "Neamt": [("Iasi", 87)]
# }


# heuristics = {
#     "Arad": 366, "Zerind": 374, "Oradea": 380, "Timisoara": 329,
#     "Lugoj": 244, "Mehadia": 241, "Dobreta": 242, "Craiova": 160,
#     "Sibiu": 253, "Rimnicu Vilcea": 193, "Fagaras": 176,
#     "Pitesti": 100, "Bucharest": 0, "Giurgiu": 77, "Urziceni": 80,
#     "Hirsova": 151, "Eforie": 161, "Vaslui": 199, "Iasi": 226,
#     "Neamt": 234
# }



graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'D': 5},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 0},
    'G': {},
    'S': {'A': 1, 'G': 10}
}

# Heuristic dictionary (no longer a function)
heuristics = {
    'A': 3, 'B': 4, 'C': 2,
    'D': 6, 'G': 0, 'S': 5
}





start=input("enter the start node:")
goal=input("enter the goal node:")

path,cost=astar(graph,heuristics,start,goal)


print(f"{path}")
print(f"{cost}")