import numpy as np
def sum_2_rows(M):
    return M[0::2]+M[1::2]
def sum_left_right(M):
    return M[:,0:(len(M)//2)]+M[:,(len(M)//2):]
def sum_upper_lower(M):
    return M[0:(len(M)//2),:]+M[(len(M)//2):,:]
def sum_4_quadrants(M):
    return M[0:(len(M)//2),0:(len(M)//2)]+M[0:(len(M)//2),(len(M)//2):len(M)]+M[(len(M)//2):len(M),0:(len(M)//2)]+M[(len(M)//2):len(M),(len(M)//2):len(M)]
def sum_4_cells(M):
    return M[::2,::2]+M[::2,1::2]+M[1::2,::2]+M[1::2,1::2]
def count_leap_years(M):
    M=M-543
    return np.count_nonzero((M % 4 == 0) & (M % 100 != 0) | (M % 400 == 0))
exec(input().strip())