def first_fit(L,e):
    if len(L)<1:
        return L.append([e])
    for i in L:
        if sum(i)+e<=100:
            i.append(e)
            L[L.index(i)]=i
            return L
    return L.append([e])
def best_fit(L,e):
    q=[]
    for x in L:
        if 100-sum(x)-e>=0:
            q.append(100-sum(x)-e)
        else:
            q.append(100)
    if len(q)>1:
        m=min(q)
        if m==100:
            L.append([e])
        else:
            L[q.index(m)].append(e)
    else:L.append([e])
def partition_FF(D):
    ans=[]
    for e in D:
        first_fit(ans,e)
    return ans
def partition_BF(D):
    ans=[[D[0]]]
    for e in D[1:]:
        best_fit(ans,e)
    return ans
exec(input().strip())