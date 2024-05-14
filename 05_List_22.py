_,l = input(),[]
while _ != 'q' :
    l+=_.split()
    _ = input()
_ = input().split()
g=['F','D','D+','C','C+','B','B+','A','A']
for i in _:
    l[l.index(i)+1] = g[g.index(l[l.index(i)+1])+1]
_ = []
for i in range(0,len(l)-1,2) :
    _.append([l[i],l[i+1]])
_.sort()
a = ''
for i in _ :
    print(i[0],i[1])