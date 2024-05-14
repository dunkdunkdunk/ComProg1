a = float(input())
L, U = 0, a
x = (U-L)/2

while abs(a-(10**x)) >= 10**-10*max(a,10**x) :
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    x = (U+L) / 2

print(round((U+L)/2,6))