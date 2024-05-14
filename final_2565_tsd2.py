from collections import OrderedDict
def f1(data):
# write your code here
    a=[]
    b=OrderedDict()
    for i in data:
        a.append(tuple([i[0],set(i[1])]))
    for i in a:
        for j in i[1]:
            if j in b.keys():b[j]+=1
            else:b[j]=1
    c=list(b.items())
    c.sort(key=lambda x:(-x[1],x[0]))
    return c
# Your code must contains this line
exec(input())