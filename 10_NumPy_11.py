import numpy as np
def get_column_from_bottom_to_top( A , c ):
    return A[::-1,c]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[-1,::2]
def get_diagonal1( A ):
    return np.diagonal(A)
def get_diagonal2( A ):
    return np.diagonal(A[::,::-1])
exec(input().strip())