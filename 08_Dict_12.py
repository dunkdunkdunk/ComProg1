d,i={},int(input())
for j in range(i):
    k=input().split()
    d[k[0]]=k[1]
    d[k[1]]=k[0]
i=int(input())
for j in range(i):
    k=input()
    if d.get(k) is not None:
        print(d.get(k))
    else: print('Not found')