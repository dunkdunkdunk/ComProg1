for i in range(int(input())):
    d=input()
    count=0
    for i in d:
        if i=='.':
            count+=1
        else:break
    print('.'*(count//2)+d[count:])