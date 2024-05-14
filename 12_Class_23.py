class Card:
    def __init__(self, value, suit):
        self.v,self.s=value,suit
    def __str__(self):
        return '('+self.v+' '+self.s+')'
    def next1(self):
        val=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suits=['club','diamond','heart','spade']
        self.tv1,self.ts1=val.index(self.v),suits.index(self.s)
        if self.ts1==len(suits)-1:
            if self.tv1==len(val)-1:
                self.ts1,self.tv1=0,0
            else:self.tv1+=1;self.ts1=0
        else:self.ts1+=1
        return Card(val[self.tv1],suits[self.ts1])
    def next2(self):
        val=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
        suits=['club','diamond','heart','spade']
        self.tv2,self.ts2=val.index(self.v),suits.index(self.s)
        if self.ts2==len(suits)-1:
            if self.tv2==len(val)-1:
                self.ts2,self.tv2=0,0
            else:self.tv2+=1;self.ts2=0
        else:self.ts2+=1
        self.s,self.v=suits[self.ts2],val[self.tv2]
n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])