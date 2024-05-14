def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:return i
def flatten(t):
    a=[]
    for i in t:
        for j in i:
            if j!=0:a.append(j)
    return a
def inversions(x):
    count=0
    for i in range(len(x)):
        for j in range(len(x)):
            if i!=j and i<=j and x[i]>x[j]:
                count+=1
    return count
def solvable(t):
    return (len(t)%2!=0 and inversions(flatten(t))%2==0) or (len(t)%2==0 and ((inversions(flatten(t))%2!=0 and row_number(t,0)%2==0) or (inversions(flatten(t))%2==0 and row_number(t,0)%2!=0)))
exec(input().strip())