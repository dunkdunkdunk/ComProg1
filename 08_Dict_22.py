d,i={},int(input())
while i!=0:
    k=input().split()
    d[k[0]]=float(k[1])
    i-=1
o,i={},int(input())
while i!=0:
    k=input().split()
    if k[0] in d.keys():
        if k[0] in o:
            o[k[0]]+=list(d.values())[list(d.keys()).index(k[0])]*float(k[1])
        else:
            o[k[0]]=list(d.values())[list(d.keys()).index(k[0])]*float(k[1])
    i-=1
t=[]
for i,j in o.items():
    if j==max(list(o.values())):
        t.append(i)
t.sort()
print("Total ice cream sales:",str(sum(o.values()))+'\n'+"Top sales:",', '.join(t))if len(o)>0 else print("No ice cream sales")
