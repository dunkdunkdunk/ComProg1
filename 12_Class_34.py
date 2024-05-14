from collections import OrderedDict
class piggybank:
    def __init__(self):
        self.coins=OrderedDict()
    def add(self, v, n):
        v=float(v)
        if n>100:return False
        else:
            if v in self.coins.keys():
                if self.coins[v]+n>100:return False
                self.coins[v]+=n
            elif v not in self.coins.keys():
                if sum(self.coins.values())+n<=100:self.coins[v]=n
                else:return False
            return sum(self.coins.values())<=100
    def __float__(self):
        ans=[i*j for i,j in self.coins.items()]
        return float(sum(ans))
    def __str__(self):
        ans=[]
        for i,j in self.coins.items():
            ans.append(str(i)+':'+str(j))
        ans.sort(key=lambda x:float((x.split(':'))[0]))
        return '{'+', '.join(ans)+'}'
cmd1=input().split(';')
cmd2=input().split(';')
p1=piggybank();p2=piggybank()
for c in cmd1:eval(c)
for c in cmd2:eval(c)