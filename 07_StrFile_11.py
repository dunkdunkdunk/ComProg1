_=input()
if _[-1] in 's x'.split() or _[-2:]=='ch':
    print(_+'es')
elif _[-1]=='y' and _[-2] not in 'a e i o u'.split():
    print(_[:-1]+'ies')
else:
    print(_+'s')