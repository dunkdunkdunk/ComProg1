t = int(input())
n = []
for i in range(t):
    n += input().split()
_ = input() == "Zig-Zag"
zig = []
zag = []
i = 0
for j in n :
    if i > 3 :
        i = 0
    if i == 0 or i == 3:
        zig.append(int(j))
        i+=1
    elif i == 1 or i == 2:
        zag.append(int(j))
        i+=1 
print(min(zig),max(zag)) if _ else print(min(zag),max(zig))