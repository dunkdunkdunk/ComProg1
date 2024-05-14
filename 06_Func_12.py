def is_prime(n):
    if n<=1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k==0:
            return False
    return True
def next_prime(N):
    if N%2==0:N+=1
    else:N+=2
    while not is_prime(N):
        N+=2
    return N
def next_twin_prime(N):
    _=[]
    while 1:
        N+=1
        if is_prime(N) and len(_)<2:
            _.append(N)
        elif len(_)==2:
            if _[1]-_[0]!=2:
                _.pop(0)
            else:
                return (_[0],_[1])
exec(input().strip())