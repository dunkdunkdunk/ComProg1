n=['0','1','2','3','4','5','6','7','8','9']
for i in input():
    n.remove(i) if i in n else None
print(",".join(n)) if len(n)>0 else print('None')