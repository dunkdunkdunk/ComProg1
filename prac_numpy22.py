import numpy as np
def mult_table(nrows,ncols):
    c=np.tile(np.arange(1,ncols+1),(nrows,1))
    r=np.tile(np.arange(1,nrows+1),(ncols,1)).T
    return c*r
exec(input().strip())