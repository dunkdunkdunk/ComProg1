_=input().split()
f,y=open(_[0],'r'),_[1][-2:]
fn=f.read().split();f1=fn[::2];f2=fn[1::2]
f.close()
data=[]
for i in range(len(f1)):
    if y==f1[i][:2]:
        data.append(float(f2[i]))
print(min(data),max(data),round(sum(data)/len(data),2)) if len(data)>0 else print("No data")