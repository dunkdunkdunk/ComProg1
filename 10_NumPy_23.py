import numpy as np
def read_data():
    w=[float(e) for e in input().split()]
    weight=np.array(w)
    n=int(input())
    data=np.ndarray((n,4),int)
    for i in range(n):
        data[i]=[int(e) for e in input().split()]
    return weight,data
def report_lower_than_mean(weight,data):
    t=np.sum(weight*data[:,1:],axis=1)
    m=np.mean(t)
    l=data[:,0][t<m]
    print("None") if len(l)<1 else print(", ".join(np.array(l,dtype=str)))
exec(input().strip())