a = input()
count = 1
answer = []
for i in range(len(a)):
    if i != len(a)-1 : 
        if a[i] == a[i+1]:
            count += 1
        else :
            answer.append(str(a[i])+" "+str(count))
            count = 1
    else :
        answer.append(str(a[i])+" "+str(count))
print((" ").join(answer))