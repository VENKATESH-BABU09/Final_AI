import heapq as h

def heuristic(x,y,goal):
    return min(abs(x-goal),abs(y-goal))
def water_jug(jug1,jug2,goal):
    visited=set()
    pq=[]
    x=0
    y=0
    parent={(x,y):(-1,-1)}
    g_cost={(x,y):0}

    h.heappush(pq,(heuristic(x,y,goal),0,x,y))

    while pq:
        f_cost,gcost,x,y=h.heappop(pq)
        if (x,y) in visited:
            continue
        visited.add((x,y))

        if x==goal or y==goal:
            path=[]
            while (x,y)!=(-1,-1):
                path.append((x,y))
                (x,y)=parent[(x,y)]
            path.reverse()
            print(path)
            return
        

        next_states=[
            (jug1,y),
            (x,jug2),
            (jug1,0),
            (0,jug2),
            (max(0,x-(jug2-y)),min(jug2,x+y)),
            (min(jug1,x+y),max(0,y-(jug1-x)))
        ]


        for next_x,next_y in next_states:
            if (next_x,next_y) not in visited:
                new_g_cost=gcost+1
                if (next_x,next_y) not in g_cost or g_cost[(next_x,next_y)]>new_g_cost:
                    parent[(next_x,next_y)]=(x,y)
                    g_cost[(next_x,next_y)]=new_g_cost
                    h.heappush(pq,(heuristic(x,y,goal)+new_g_cost,new_g_cost,next_x,next_y))

    print("not reachable")







jug1=int(input("jug1:"))
jug2=int(input("jug2:"))
goal=int(input("goal:"))

water_jug(jug1,jug2,goal)