d,i={},int(input())
for j in range(i):
    k=input().split()
    d[k[0]+' '+k[1]]=k[2]
    d[k[2]]=k[0]+' '+k[1]
i=int(input())
for j in range(i):
    k=input()
    if d.get(k) is not None:
        print(k+' --> '+d.get(k))
    else: print(k+' --> '+'Not found')