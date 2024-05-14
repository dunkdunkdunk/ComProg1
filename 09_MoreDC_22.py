def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        x=input().split()
        r=[]
        for e in x:
            r.append(float(e))
        m.append(r)
    return m
def mult_c(c,A):
    a=[]
    for i in A:
        b=[]
        for j in i:
            b.append(j*c)
        a.append(b)
    return a
def mult(A,B):
    ans=[]
    for row in range(len(A)):
        r=[]
        col=0
        while col<len(B[0]):
            s=0
            iden=0
            for i in A[row]:
                s+=(B[iden][col]*i)
                iden+=1
            r.append(s)
            col+=1
        ans.append(r)
    return ans
            
exec(input().strip())


    # m,n=len(A),len(B[0])
    # ans=[]
    # sn,c,d=0,0,0
    # for t in range(n): 
    #     r=[]   
    #     for i in range(n):
    #         for j in range(m):
    #             sn+=float(A[i][d])*float(B[j][c])
    #             d+=1
    #         d=0
    #         c+=1
    #         r.append(sn)
    #         sn=0
    #     ans.append(r)
    # print(sn)
    # return ans