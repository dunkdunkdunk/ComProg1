station={}
while True:
    k=input().split()
    if len(k)<2:break
    else:
        if not k[0] in station.keys():
            station[k[0]]={k[1]}
        else:
            station[k[0]].add(k[1])
        if not k[1] in station.keys():
            station[k[1]]={k[0]}
        else:
            station[k[1]].add(k[0])
ans=set(k)
for i in station:
    if i==k[0]:
        for j in station[i]:
            ans.add(j)
            if j in station.keys():
                for k in station[j]:
                    ans.add(k)
ans=list(ans)
ans.sort()
for i in ans:
    print(i)