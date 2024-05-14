w,l=[],[]
for i in range(int(input())):
    p=input().split()
    w.append(p[0]);l.append(p[1])
print(sorted(set(w).difference(set(l))))