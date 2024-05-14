from collections import OrderedDict
def f2(data):
    newdata=OrderedDict()
    for i in data:
        d=[]
        for j in list(i['answers'].items()):
            d.append(str(j[0])+j[1])
        newdata[i['student_id']]=d
    mem=OrderedDict()
    it=list(newdata.items())
    count=1
    high=0
    for i in it:
        short=[]
        for j in it:
            short.append(round(len(set(i[1]).intersection(set(j[1])))/len((set(i[1]).union(set(j[1])))),2))
        short=[0]*count+short[count:]
        count+=1
        if max(short)>high:high=max(short)
        mem[i[0]]=short
    take=[]
    for i in mem:
        if high in mem[i]:
            tail=[]
            for j in range(len(mem[i])):
                if mem[i][j]==high:
                    tail.append(j)
            take.append([i,tail])
    ans=[]
    for i in take:
        for j in i[1]:
            ans.append(tuple([i[0],list(newdata.keys())[j]]))
    return ans
exec(input())
# print(sorted(f2([{"student_id": 1, "answers": {1: "A", 2: "B", 3: "C"}},{"student_id": 2, "answers": {1: "A", 2: "B", 3: "D"}},{"student_id": 3, "answers": {1: "A", 2: "B", 3: "C", 4: "D"}},{"student_id": 4, "answers": {2: "B", 3: "C", 4: "D"}},{"student_id": 5, "answers": {3: "C", 4: "D"}}])))
# print(sorted(f2([ {"student_id": 1, "answers": {1: "A", 2: "B", 3: "C"}},{"student_id": 2, "answers": {1: "A", 2: "B", 3: "C"}},{"student_id": 3, "answers": {1: "A", 2: "B", 3: "C"}},{"student_id": 4, "answers": {1: "A", 2: "B", 3: "C"}},]))) 