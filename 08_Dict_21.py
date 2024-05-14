p,d=input().lower(),{}
for i in p:    
    if i.isalpha():
        if i in d:
            d[i]+=1
        else:
            d[i]=1
ans=[]
for i in d:
    ans.append([-d[i],i])
ans.sort()
for i,j in ans:
    print(str(j)+' -> '+str(-i))