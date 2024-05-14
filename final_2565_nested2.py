def is_armstrong():
    a=[]
    p=input()
    while p!='q':
        a.append(p)
        p=input()
    ans=[]
    for i in a:
        l=len(i)
        b=0
        for j in i:
            b+=int(j)**len(i)
        ans.append(i==str(b))
    return '\n'.join(list(map(str,ans)))
cmd = input().strip().split('; ')
for c in cmd: exec(c)
