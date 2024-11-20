import _heapq as h


def print_state(state):
    for i in range(0,9,3):
        print(state[i], state[i+1], state[i+2])
        
    print()

def heuristic(start,goal):
    distance=0
    for i in range(1,9):
        s=start.index(i)
        g=goal.index(i)

        r1,c1=divmod(s,3)
        r2,c2=divmod(g,3)

        distance+=abs(r2-r1)+abs(c2-c1)

    return distance


def next_states(curr_state):
    next_state=[]
    blank=curr_state.index(0)
    r1,c1=divmod(blank,3)

    distances=[(1,0),(-1,0),(0,1),(0,-1)]


    for r,c in distances:
        newr,newc=r1+r,c1+c
        if 0<=newr<3 and 0<=newc<3:
            newblank=newr*3+newc
            new_state=list(curr_state)
            new_state[blank],new_state[newblank]=new_state[newblank],new_state[blank]

            next_state.append(tuple(new_state))

    return next_state


def astar(start,goal):
    vis=set()
    pq=[]
    h.heappush(pq,(heuristic(start,goal),0,start,[]))

    while pq:
        f_cost,g_cost,curr_state,path=h.heappop(pq)

        if curr_state in vis:
            continue
        vis.add(curr_state)


        if curr_state==goal:
            print("goal reached")
            for st in path+[curr_state]:
                print_state(st)
            print(goal)
            return
        
        for next_state in next_states(curr_state):
            if next_state not in vis:
                new_g=g_cost+1
                h.heappush(pq,(heuristic(next_state,goal)+new_g,new_g,next_state,path+[curr_state]))
    print("Goal not reached")
    return None



start = (1,2,3,5,6,0,7,8,4)
goal = (1,2,3,4,5,6,7,8,0)


astar(start,goal)

