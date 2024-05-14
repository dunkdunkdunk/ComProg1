import numpy as np
def f3(data):
    b=data<np.array([data.max(axis=1)]).T
    data_clone1=data.copy()
    data_clone

    c=data==np.array([data.max(axis=1)]).T
    data_clone2=data.copy()
    data_clone2[c]=0
    d=data_clone2<np.array([data_clone2.max(axis=1)]).T
    data_clone3=data_clone2.copy()
    data_clone3[d]=0
    return data_clone1+data_clone3
exec(input())