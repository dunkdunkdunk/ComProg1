alpha = 'abcdefghijklmnopqrstuvwsyz'
ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
with open('data.txt','w') as f:
    while True:
        line = input()
        if line == 'end':
            break
        f.writelines(line)

with open('data.txt','r') as f:
    lines = f.readlines()
    for line in lines:
        ans=''
        for cha in line:
            if cha in alpha:
                index = alpha.index(cha)
                if index+13 >=26:
                    index-=26
                ans+=alpha[index+13]
            elif cha in ALPHA:
                index = ALPHA.index(cha)
                if index+13 >=26:
                    index-=26
                ans+=alpha[index+13]
            else:
                ans+=alpha[index]
        print(ans)