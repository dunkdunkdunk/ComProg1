# i = set([int(i) for i in input().split()])
# print(len(i))
# print(sorted(i)[0:10])

i=[int(i) for i in input().split()]
i.sort()
count=1
c=i[0]
a=[c]
for j in i:
    if c!=j:
        count+=1
        c=j
        a.append(c)
print(count)
print(sorted(a)[0:10])