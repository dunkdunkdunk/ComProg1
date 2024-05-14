from collections import OrderedDict
c,t,d=open(input(),'r').readlines(),open(input(),'r').readlines(),open(input(),'r').readlines()
cc,tt,dd=[],[],[]
for i in c:
    cc.append(i.strip())
for i in t:
    tt.append(i.strip())
for i in d:
    dd.append(i.strip())
# print(cc,tt,dd)
cd,td=OrderedDict(),OrderedDict()
for i in cc:
    i=i.split(',')
    cd[i[0]]=i[1]
for j in tt:
    j=j.split(',')
    td[j[0]]=j[1]
# print(cd,td)
for i in dd:
    i=i.split(',')
    if i[0] in cd.keys() and i[1] in td.keys():
        print(str(cd[i[0]])+','+str(td[i[1]]))
    else:
        print('record error')