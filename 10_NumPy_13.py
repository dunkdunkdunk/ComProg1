import numpy as np
def p(x):
    return 1/(1+np.e**(3.98-(0.1*x[:,0])-(0.5*x[:,1])))
exec(input().strip())