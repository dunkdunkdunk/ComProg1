def distance1(x1,y1,x2,y2):
    dx,dy=abs(x1-x2),abs(y1-y2)
    return (dx*dx+dy*dy)**0.5
def distance2(p1,p2):
    dx,dy=abs(p1[0]-p2[0]),abs(p1[1]-p2[1])
    return (dx*dx+dy*dy)**0.5
def distance3(c1,c2):
    dx,dy,dr=abs(c1[0]-c2[0]),abs(c1[1]-c2[1]),c1[2]+c2[2]
    d=(dx*dx+dy*dy)**0.5
    return d, d<=dr
def perimeter(points):
    points+=[points[0]];_=0
    for i in range(len(points)):
        if i!=len(points)-1:
            dx,dy=abs(points[i][0]-points[i+1][0]),abs(points[i][1]-points[i+1][1])
            _+=(dx*dx+dy*dy)**0.5
        elif i==len(points)-1:
            return _
exec(input().strip())