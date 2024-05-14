coor=[]
for i in range(int(input())):
    _,__ = map(float,input().split())
    coor.append([(_*_+__*__)**0.5,str(i+1),str(_),str(__)])
coor.sort()
print('#{}: ({}, {})'.format(str(coor[2][1]),coor[2][2],coor[2][3]))