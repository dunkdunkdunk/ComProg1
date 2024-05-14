#write method "search".
def show(d):
    for e in d:
        print(e)
def search(m, keyword, power):
    a=[]
    if keyword=='-' and power=='-':return m
    elif keyword!='-' and power=='-':
        for i in m:
            if keyword in i[0] or keyword in i[1]:
                a.append(i)
    elif keyword=='-' and power!='-':
        for i in m:
            if power==str(i[2]):
                a.append(i)
    else:
        for i in m:
            if (keyword in i[0] or keyword in i[1]) and power==str(i[2]):
                a.append(i)
    return a
m1 = ["green giant", "sacrifice a monster: draw a card", 5]
m2 = ["blue giant", "tap: draw a card, then discard a card" , 3]
m3 = ["blue drake", "discard a card: return to hand", 1]
m4 = ["green drake", "sacrifice a land: destroy target giant", 3]
m5 = ["black wurm", "sacrifice a permanent: destroy target permanent", 3]
m = [m1,m2,m3,m4,m5]
exec(input())