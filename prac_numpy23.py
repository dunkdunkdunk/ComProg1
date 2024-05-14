import numpy as np
def read_data():
    w=[float(e) for e in input().split()]
    weight=np.array(w)
    n=int(input())
    data=np.ndarray((n,4),int)
    for i in range(n):
        data[i]=[int(e) for e in input().split()]
    print(weight,data)
    return weight,data
def report_lower_than_mean(weight,data):
    return

exec(input())
# cmd='''w,d = read_data(); report_lower_than_mean(w,d)
# 0.25 0.5 0.25
# 6
# 619111 80 90 70
# 619121 80 90 70
# 619131 80 90 70
# 619141 80 90 70
# 619151 80 90 70
# 619161 80 90 70'''