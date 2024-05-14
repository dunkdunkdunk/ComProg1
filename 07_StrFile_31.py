_,c=input().upper(),input()
if c=='R':
    a=''
    for i in _:
        if i=='A':a+='T'
        elif i=='C':a+='G'
        elif i=='G':a+='C'
        elif i=='T':a+='A'
    print(a[-1::-1])
elif c=='F':
    a,c,t,g,e=0,0,0,0,0
    for i in _:
        if i=='A':a+=1
        elif i=='C':c+=1
        elif i=='G':g+=1
        elif i=='T':t+=1
        else:e=1
    print('A={}, T={}, G={}, C={}'.format(a,t,g,c)) if e!=1 else print('Invalid DNA')
elif c=='D':
    a,f,e=0,input(),False
    for i in range(len(_)):
        if not _[i].upper() in 'ATCG':
            e=not e
        if i==len(_)-1:
            break
        elif _[i]+_[i+1]==f:
            a+=1
    print(a) if not e else print('Invalid DNA')
    