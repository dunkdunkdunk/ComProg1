import numpy as np
def mult_table(nrows,ncols):
    return np.arange(1,ncols+1)*np.arange(1,nrows+1).reshape(-1,1)
exec(input().strip())