import heapq as h

graph={
    'S':['A','B'],
    'A':['C','D'],
    'B':['E','F'],
    'C':[],
    'D':[],
    'E':['H'],
    'F':['I','G']
}

heuristics={
    'S':13,
    'A':12,
    'B':4,
    'C':7,
    'D':3,
    'E':8,
    'F':2,
    'H':4,
    'I':9,
    'G':0
}


def bfs(graph,heuristics,start,goal):
    pq=[]

    h.heappush(pq,(heuristics[start],start,[start]))

    while pq:
        curr_h,curr,path=h.heappop(pq)
        if curr==goal:
            print("we reached goal")
            return path
        for neigh in graph[curr]:
            h.heappush(pq,(heuristics[neigh],neigh,path+[neigh]))
    return None




start='S'
goal='G'

path=bfs(graph,heuristics,start,goal)
print("path:")
print(path)