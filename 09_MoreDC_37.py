dep={}
for i in range(int(input())):
    k=input().split()
    dep[k[0]]=int(k[1])
stu=[]
for i in range(int(input())):
    k=input().split()
    stu.append(tuple((int(k[0]),float(k[1]),k[2],k[3],k[4],k[5])))
stu.sort(key=lambda x:x[1])
stu.reverse()
ans=[]
for i in stu:
    indexx=2
    while indexx<=5:
        if dep[i[indexx]]>0:
            ans.append(tuple((i[0],i[indexx])))
            dep[i[indexx]]-=1
            break
        else:
            indexx+=1
ans.sort(key=lambda x:x[0])
for i,j in ans:
    print(i,j)