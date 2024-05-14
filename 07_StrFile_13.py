_,a=input(),''
for i in _:
    if not i.isalnum():a+=' '
    else:a+=i
_,a='',a.split()
for i in range(len(a)):
    if i==0:_+=a[i].lower()
    else:_+=a[i][0].upper()+a[i][1:].lower()
print(_)