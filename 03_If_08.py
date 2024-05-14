a = int(input())
b = int(input())
c = int(input()) - 543

day = [31,28,31,30,31,30,31,31,30,31,30,31][0:b]
day.pop()

if b >= 2 :
    leap = False
    if c % 400 == 0 :
        leap = True
    elif c % 4 == 0 and c % 100 != 0 :
        leap = True
if leap : a += 1

print(sum(day)+a)