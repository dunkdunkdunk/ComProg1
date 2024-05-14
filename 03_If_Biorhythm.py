import math
bd, bm, by, d, m, y  = [int(e)for e in input().split()]
i = [31,28,31,30,31,30,31,31,30,31,30,31]

j = i[0:m]
j.pop()

if bm <= 2 :
    if (by-543) % 400 == 0 : bd -= 1
    elif (by-543) % 4 == 0 and (by-543) % 100 != 0 : bd -= 1

if m > 2 :
    if (y-543) % 400 == 0 : d += 1
    elif (y-543) % 4 == 0 and (y-543) % 100 != 0 : d += 1

total = (i[bm-1]-bd+1+sum(i[bm:])) + ((y - by - 1) * 365) + (sum(j)+d-1)
print(total,"{:.2f}".format(math.sin((2*math.pi*total)/23)),"{:.2f}".format(math.sin((2*math.pi*total)/28)),"{:.2f}".format(math.sin((2*math.pi*total)/33)))