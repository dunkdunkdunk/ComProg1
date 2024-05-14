def total(pocket):
    total=0
    for i,j in pocket.items():
        total+=i*j
    return total
def take(pocket,money_in):
    for i,j in money_in.items():
        if i in pocket:pocket[i]+=j
        else:pocket[i]=j
    return pocket
def pay(pocket,amt):
    money_out={}
    for m in sorted(pocket.keys())[::-1]:
        if amt>=m:
            c=min(pocket[m],amt//m)
            money_out[m]=c
            pocket[m]-=c
            amt-=m*c
    if amt>0:
        take(pocket,money_out)
        money_out={}
    return money_out

exec(input().strip())