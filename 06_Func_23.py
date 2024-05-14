def make_int_list(x):
    return [int(i) for i in x.split()]
def is_odd(e):
    return e%2!=0
def odd_list(alist):
    a=[]
    for i in alist:
        a.append(i) if i%2!=0 else None
    return a
def sum_square(alist):
    a=0
    for i in alist:
        a+=i*i
    return a
exec(input().strip())