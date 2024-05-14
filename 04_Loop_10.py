a = float(input())
L, U, _ = 0, 0, a
while _ != 0 :
    _ = _ // 10
    U+=1
x = U/2
while abs(a - 10**x) >= 1e-10 * max(a, 10**x) :
    if 10**x > a:
        U = x
    elif 10**x < a:
        L = x
    x = (U + L) / 2
print(round((U+L)/2,6))