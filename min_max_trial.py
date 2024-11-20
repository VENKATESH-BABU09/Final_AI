import math

def min_max(cd,node,src,maxt,td):
    if cd==td:
        return src[node]
    
    left=min_max(cd+1,node*2,src,not maxt,td)
    right=min_max(cd+1,node*2+1,src,not maxt,td)


    if left is None:
        return right
    if right is None:
        return left
    

    return max(left,right) if maxt else min(left,right)


src=list(map(int,input("enter the leaf nodes:").strip().split()))

n=len(src)
next_2=2**math.ceil(math.log2(n))
src.extend([None]*(next_2-n))
td=math.ceil(math.log2(len(src)))

cd=0
node=0
maxt=True

op=min_max(cd,node,src,maxt,td)

print("the optimum node: ",op)