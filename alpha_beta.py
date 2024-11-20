import math


def alph_beta(cd,src,node,maxt,alpha,beta,td,depth=0):
    if cd==td:
        return src[node]
    if maxt:
        maxval=float('-inf')
        value=alph_beta(cd+1,src,node*2,False,alpha,beta,td,depth+1)
        maxval=max(maxval,value)
        alpha=max(alpha,maxval)
        if alpha>=beta:
            print("the pruning happens")
            return maxval
        value=alph_beta(cd+1,src,node*2+1,False,alpha,beta,td,depth+1)
        maxval=max(maxval,value)
        alpha=max(alpha,maxval)
        if alpha>=beta:
            print("pruning happens")
            return maxval
        return maxval
    else:
        minval=float('inf')
        value=alph_beta(cd+1,src,node*2,True,alpha,beta,td,depth+1)
        minval=min(minval,value)
        beta=min(beta,minval)
        if alpha>=beta:
            print("the pruning happens")
            return minval
        value=alph_beta(cd+1,src,node*2+1,True,alpha,beta,td,depth+1)
        minval=min(minval,value)
        beta=min(beta,minval)
        if alpha>=beta:
            print("pruning happens")
            return minval
        return minval
        
src=list(map(int,input("enter the leaves nodes:").split()))
n=len(src)
next_2=2**math.ceil(math.log2(n))

src.extend([None]*(next_2-n))

td=math.ceil(math.log2(len(src)))

cd=0
node=0
alpha=float('-inf')
beta=float('inf')
maxt=True


op=alph_beta(cd,src,node,maxt,alpha,beta,td)

print(op)