def factor(N):
    ans=[]
    for i in range(2,N+1):
        count=0
        while N%i==0:
            N=N//i
            count+=1
        if count>0:ans.append([i,count])
    return ans
exec(input().strip())