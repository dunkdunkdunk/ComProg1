n=''
_=input()
while len(_.split())>1:
    n += _.split()[0]+" "+_.split()[1]+" "
    _ = input()
zig,zag,i = '','',0
for j in n.split() :
    if i>3 :
        i = 0
    if i==0 or i==3:
        zig+=j+" "
        i+=1
    elif i==1 or i==2:
        zag+=j+" "
        i+=1 
a,b=[int(i) for i in zig.split()],[int(i) for i in zag.split()]
print(min(a),max(b)) if _=="Zig-Zag" else print(min(b),max(a))