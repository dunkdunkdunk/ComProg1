n=int(input())
a=[]
a.append(str(n))
while n!=1:
    if n%2==0:
        n=n//2
    else:
        n=(3*n)+1
    a.append(str(n))
print('->'.join(a[-15:])) if len(a) >15 else print('->'.join(a))