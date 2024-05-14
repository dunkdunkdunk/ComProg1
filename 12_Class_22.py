class Card:
    def __init__(self,value,suit):
        self.v=value
        self.s=suit
    def __str__(self):
        return '('+self.v+' '+self.s+')'
    def getScore(self):
        if self.v=='A':self.score=1
        elif self.v in ['J','Q','K']:self.score=10
        else:self.score=self.v
        return self.score
    def sum(self,other):
        return (int(self.score)+int(other.score))%10
    def __lt__(self,rhs):
        val=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suit=['club','diamond','heart','spade']
        if self.v!=rhs.v:return(val.index(str(self.v))<val.index(str(rhs.v)))
        else:return(suit.index(self.s)<suit.index(rhs.s))
n=int(input())
cards=[]
for i in range(n):
    value,suit=input().split()
    cards.append(Card(value,suit))
for i in range(n):
    print(cards[i].getScore())
print("----------") 
for i in range(n-1): 
    print(Card.sum(cards[i], cards[i+1]))
print("----------") 
cards.sort() 
for i in range(n): 
    print(cards[i]) 