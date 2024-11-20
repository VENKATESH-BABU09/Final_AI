import heapq as h

def heuristic(x,y,goal):
    return min(abs(x-goal),abs(y-goal))

def astar(jug1,jug2,goal):

    visited=set()
    pq=[]
    x=0
    y=0
    parent={(x,y):(-1,-1)}
    g_cost={(x,y):0}

    h.heappush(pq,(heuristic(x,y,goal),0,x,y))

    while pq:
        f_cost,g_costval,x,y=h.heappop(pq)

        if (x,y) in visited:
            continue
        visited.add((x,y))

        if(x==goal or y==goal):
            path=[]
            while (x,y)!=(-1,-1):
                path.append((x,y))
                (x,y)=parent[(x,y)]
            path.reverse()
            return path
        

        next_states=[
            (jug1,y),
            (x,jug2),
            (0,y),
            (x,0),
            (max(0,x-(jug2-y)),min(jug2,x+y)),
            (min(jug1,x+y),max(0,y-(jug1-x)))
        ]


        for next_x,next_y in next_states:
            if (next_x,next_y) not in visited:
                # visited.add((next_x,next_y))
                new_gcost=g_costval+1

                if (next_x,next_y) not in g_cost or new_gcost<g_cost[(next_x,next_y)]:
                    parent[(next_x,next_y)]=(x,y)
                    g_cost[(next_x,next_y)]=new_gcost

                    h.heappush(pq,(heuristic(next_x,next_y,goal)+new_gcost,new_gcost,next_x,next_y))

    print("not reached")
    return None                    










jug1=int(input("enter the capacity of jug1:"))
jug2=int(input("enter the capacity of jug2:"))

goal=int(input("enter the goal amount of water you want to achieve:"))
p=astar(jug1,jug2,goal)

print(f"{p}")