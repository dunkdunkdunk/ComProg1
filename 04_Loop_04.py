a = input()
answer = ""
for i in range(len(a)) :
    if a[i] == "(" :
        answer += "["
    elif a[i] == "[" :
        answer += "("
    elif a[i] == ")" :
        answer += "]"
    elif a[i] == "]" :
        answer += ")"
    else :
        answer += a[i]
print(answer)