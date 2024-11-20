import math

def alpha_beta(cd,node,src,maxt,alpha,beta,td,depth=0):
    if cd==td:
        return src[node]
    
    if maxt:
        maxval=float('-inf')
        val=alpha_beta(cd+1,node*2,src,False,alpha,beta,td,depth+1)
        maxval=max(maxval,val)
        alpha=max(alpha,val)
        if alpha>=beta:
            print(f"pruning happens at depth {depth+1} ")
            return maxval
        val=alpha_beta(cd+1,node*2+1,src,False,alpha,beta,td,depth+1)
        maxval=max(maxval,val)
        alpha=max(alpha,val)
        if alpha>=beta:
            print(f"pruning happens at depth {depth+1} ")
            return maxval
        return maxval
    else:
        minval=float('inf')
        val=alpha_beta(cd+1,node*2,src,True,alpha,beta,td,depth+1)
        minval=min(minval,val)
        beta=min(beta,minval)
        if alpha>=beta:
            print(f"pruning happens at depth {depth+1} ")
            return minval
        val=alpha_beta(cd+1,node*2+1,src,True,alpha,beta,td,depth+1)
        minval=min(minval,val)
        beta=min(beta,val)
        if alpha>=beta:
            print(f"pruning happens at depth {depth+1} ")
            return minval
        return minval
        


src=list(map(int,input().strip().split()))

n=len(src)
next_2=2**math.ceil(math.log2(n))
src.extend([None]*(next_2-n))
cd=0
maxt=True
td=math.ceil(math.log2(len(src)))
alpha=float('-inf')
beta=float('inf')
node=0

op=alpha_beta(cd,node,src,maxt,alpha,beta,td)

print("the optimum node ",op)