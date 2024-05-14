a = 0
count = 0
i = input()
while i != 'q':
    a+=float(i)
    i = input()
    count+=1
print(round(a/count,2)) if a>0 else print("No Data")