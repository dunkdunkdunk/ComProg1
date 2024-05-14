q,tl,n,j,t,c=[],[],0,0,0,0
for i in range(int(input())) :
    _=input().split()
    if _[0]=="reset":
        n=_[1]
    elif _[0]=="new":
        print("ticket",n)
        q.append(int(n))
        tl.append(_[1])
        n=int(n)+1
    elif _[0]=="next":
        print("call",q[j])
        j+=1
    elif _[0]=="order":
        print("qtime",q[j-1],int(_[1])-int(tl[j-1]))
        t+=int(_[1])-int(tl[j-1])
        c+=1
    elif _[0]=="avg_qtime":
        print("avg_qtime",t/c)