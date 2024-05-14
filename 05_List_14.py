data,c=[int(i) for i in input().split()],0
for i in range(1,len(data)):
    if i<len(data)-1:
        if data[i-1]<data[i] and data[i]>data[i+1]:
            c+=1
print(c)