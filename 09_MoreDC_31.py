def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
def is_coprime(a,b,c):
    return 1 in [gcd(a,b),gcd(b,c),gcd(a,c)]
def primitive_Pythagorean_triples(max_len):
    n,m=1,2
    triple=[]
    for m in range(max_len+1):
        for n in range(1,m):
            a,b,c=m*m-n*n,2*m*n,m*m+n*n
            if is_coprime(a,b,c) and a<max_len and b<max_len and c<max_len:
                triple.append(sorted([a,b,c]))
    return sorted(triple,key=lambda x:(x[-1],x[0]))
exec(input().strip())