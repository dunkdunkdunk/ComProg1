_,p,q,r='ABCDEFGHIJKLMNOPQRSTUVWXYZ',input(),'',[]
while p!='end':
    for i in p:
        if not i.isalpha() or i.isnumeric():q+=i
        else:
            a=_.index(i.upper())+13
            if i.islower():
                if a>25:q+=_[a-26].lower()
                else:q+=_[a].lower()
            else:
                if a>25:q+=_[a-26]
                else:q+=_[a]
    r.append(q);q=''
    p=input()
print('\n'.join(r))