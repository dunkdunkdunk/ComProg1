h = int(input())
print(' '*(h-1)+"*")
for i in range(1,h-1):
    print(' '*(h-i-1)+'*',end="")
    print(' '*((2*i)-1)+'*')
print('*'*((2*h)-1),end="")