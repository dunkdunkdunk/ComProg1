def knows(R,x,y):
    return y in R[x]
def is_celeb(R,x):
    return (len(R[x])<2 and x in R[x]) or (R[x]==set())
def find_celeb(R):
    c=[]
    for x in R:
        if is_celeb(R,x):
            c.append(x)
    if len(c)>1 or len(c)==0:return None
    else:return c[0] 
def read_relations():
    R=dict()
    while True:
        d=input().split()
        if len(d)==1:break
        else:
            if not d[0] in R.keys():
                R[d[0]]=set()
                R[d[0]].add(d[1])
                if not d[1] in R.keys():
                    R[d[1]]=set()
            else:
                R[d[0]].add(d[1])
    return R
def main():
    R=read_relations()
    c=find_celeb(R)
    if c==None:
        print('Not Found')
    else:
        print(c)
exec(input().strip())