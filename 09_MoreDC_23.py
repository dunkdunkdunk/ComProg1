a={}
for i in range(int(input())):
    j,k=input().split(',')[-2:]
    k=k.split(':')
    if not j in a.keys():
        a[j]=k
    else:
        a[j]=[int(a[j][0])+int(k[0]),int(a[j][1])+int(k[1])]
a=sorted(a,key=lambda x:x[-1])
for i,j in a.items():
    m,s=int(j[0]),int(j[1])
    if s>=60:
        m+=s//60
        s=str(s%60)
        if len(s)<2:s='0'+s
    print(i,'-->',str(m)+':'+str(s))