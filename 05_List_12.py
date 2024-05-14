a,b=[],['Robert', 'Dick','William', 'Bill', 'James', 'Jim', 'John', 'Jack','Margaret', 'Peggy', 'Edward', 'Ed', 'Sarah', 'Sally', 'Andrew', 'Andy', 'Anthony', 'Tony', 'Deborah', 'Debbie']
for i in range(int(input())):
    _=input()
    if _ not in b:a.append("Not found")  
    elif b.index(_)%2!=0:a.append(b[b.index(_)-1])
    elif b.index(_)%2==0:a.append(b[b.index(_)+1])
print('\n'.join(b))