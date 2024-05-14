class roman:
    def __init__(self, r):
        letter={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        self.original=r
        self.a=0
        i=0
        while i<len(r):
            if i==len(r)-1:self.a+=letter[r[i]];break
            if letter[r[i]]<letter[r[i+1]]:self.a+=letter[r[i+1]]-letter[r[i]];i+=2
            else:self.a+=letter[r[i]];i+=1
    def __lt__(self, rhs):
        return self.a<rhs.a
    def __str__(self):
        vals=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        ans=''
        for v,c in vals:
            k=self.a//v
            ans+=k*c
            self.a-=k*v
            if self.a==0:break
        return ans
    def __int__(self):
        return self.a
    def __add__(self, rhs):
        a=self.a+rhs.a
        r=roman('I')
        r.a=a
        return r
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))