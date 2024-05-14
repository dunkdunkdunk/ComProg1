from collections import OrderedDict
a=OrderedDict()
for i in range(int(input())):
    k=input().split(':')
    a[k[0]]=set(''.join(k[1].split(' ')).split(','))
n=input()
d=a[n]
p=[]
for i in a:
    if len(d.intersection(a[i]))>0 and i!=n:
        p.append(i)
if len(p)>0:
    for i in p:
        print(i)
else: print("Not Found")