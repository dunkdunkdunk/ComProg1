d = [int(a) for a in input().split()]
p, i, j, n = d[-1], -1, 0, len(d)
while j < n:
    if d[j] <= p:
        i+=1
        d[i],d[j] = d[j],d[i]
    j+=1
print(d)