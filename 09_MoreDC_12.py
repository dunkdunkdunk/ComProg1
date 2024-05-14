a=[]
for i in range(int(input())):
    a.append(set(input().split()))
if len(a)>0:
    ku,ki=a[0],a[0]
    for i in a:
        ku,ki=ku.union(i),ki.intersection(i)
    print(len(ku))
    print(len(ki))
else:
    print(len(a))
    print(len(a))