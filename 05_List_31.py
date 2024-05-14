a = input().split()
c = a
for i in range(len(input())):
    if b[i] == "C":
        c = c[len(c)//2:]+c[0:len(c)//2]
    elif b[i] == "S":
        front = c[0:len(c)//2]
        back = c[len(c)//2:]
        c=[]
        for j in range(len(front+back)//2):
            c.append(front[j])
            c.append(back[j])
print(" ".join(c))