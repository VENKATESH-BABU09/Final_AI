import math


def min_max(cd,node,maxt,src,td):
    if cd==td:
        return src[node]
    
    left=min_max(cd+1,node*2,not maxt,src,td)
    right=min_max(cd+1,node*2+1,not maxt,src,td)

    if left is None:
        return right
    if right is None:
        return left
    
    return max(left,right) if maxt else min(left,right)

src=list(map(int,input().strip().split()))

cd=0
node=0
n=len(src)
next_2=2**math.ceil(math.log2(n))
src.extend([None]*(next_2-n))

td=math.ceil(math.log2(len(src)))
maxt=True

print("Total depth:")
print(td)

print(src)

op=min_max(cd,node,maxt,src,td)
print("optimum value: ",op)
