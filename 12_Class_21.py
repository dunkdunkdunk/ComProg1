class Complex:
    def __init__(self,a,b):
        self.real=a
        self.image=b
    def __str__(self):
        if self.real==0:
            self.real=''
        if self.image==0:
            self.image=''
        elif self.image==1:
            if self.real=='':self.image='i'
            else:self.image='+i'
        elif self.image==-1:
            self.image='-i'
        elif self.image<0:
            self.image=str(self.image)+'i'
        elif self.image>0:
            if self.real=='':self.image=str(self.image)+'i'
            else:self.image='+'+str(self.image)+'i'
        ans=str(self.real)+str(self.image)
        return '0' if ans=='' else ans
    def __add__(self,rhs):
        return Complex(self.real+rhs.real,self.image+rhs.image)
    def __mul__(self,rhs):
        return Complex((self.real*rhs.real)-(self.image*rhs.image),(self.real*rhs.image)+(self.image*rhs.real))
    def __truediv__(self,rhs):
        return Complex(((self.real*rhs.real)+(self.image*rhs.image))/((rhs.real*rhs.real)+(rhs.image*rhs.image)),(-(self.real*rhs.image)+(self.image*rhs.real))/((rhs.real*rhs.real)+(rhs.image*rhs.image)))
t,a,b,c,d=[int(x) for x in input().split()]
c1=Complex(a,b)
c2=Complex(c,d)
if t==1:print(c1)
elif t==2:print(c2)
elif t==3:print(c1+c2)
elif t==4:print(c1*c2)
else:print(c1/c2)