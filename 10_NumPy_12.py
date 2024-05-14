import numpy as np
def toCelsius(f):
    return (f-32)*(5/9)
def BMI(wh):
    return np.array(wh[::1,0]/np.power(wh[::1,1]/100,2))
def distanceTo(P, p):
    p=p-P
    return np.array(np.sqrt(np.power(p[::1,0],2)+np.power(p[::1,1],2)))
exec(input().strip())