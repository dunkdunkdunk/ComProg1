import numpy as np
# Part 2 Q1 (DO NOT DELETE this line or add line before this)
def f1(a):
# !!! YOUR CODE HERE !!!
    r=np.array_split(a,3)
    sr=a.shape[1]//3
    return(r[1])[:,:sr]-(r[1])[:,-sr:]
# main
a = np.array([int(x) for x in input().split()])
r,c = [int(x) for x in input().split()]
a = a.reshape(r,c)
print(f1(a))

# 1 2 3 4 5 6 7 8 9 10 11 12 32 22 15 16 17 18 56 11 21 22 66 24 25 26 27 28 29 30 31 32 33 34 35 36
# 6 6