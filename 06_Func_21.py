def read_answers():
    _=[]
    for i in range(int(input())):
        s,a=input().split()
        _.append([s,a])
    return _
def marking(_,__):
    s=0
    for i in range(len(_)):
        if _[i]==__[i]:
            s+=1
    return s
def grading(s):
    g=[[80,'A'],[70,'B'],[60,'C'],[50,'D']]
    for _,__ in g:
        if s>=_:return __ 
    return 'F'
def scoring(_,__):
    l=[]
    for i,j in _:
        s=marking(j,__)/len(__)*100
        g=grading(s)
        l.append([i,s,g])
    return l
def report(_):
    for i,j,k in _:
        print(i,j,k)
def sort(_):
    x=[]
    for i,j,k in _:
        x.append([j,i,k])
    x.sort()
    for i in range(len(x)):
        _[i]=[x[i][1],x[i][0],x[i][2]]
    _.reverse()
    return _
    
_=input();report(sort(scoring(read_answers(),_)))