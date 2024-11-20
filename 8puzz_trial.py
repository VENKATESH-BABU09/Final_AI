import heapq as h


def heuristic(start,goal):
    distance=0
    for i in range(1,9):
        s=start.index(i)
        g=goal.index(i)
        r1,c1=divmod(s,3)
        r2,c2=divmod(g,3)
        distance+=abs(r2-r1)+abs(c2-c1)

    return 

def astar(start,goal):
    vis=set()
    pq=[]
    h.heappush(heuristic(start,goal))





start=
goal=
astar(start,goal)