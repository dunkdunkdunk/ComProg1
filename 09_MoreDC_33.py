def pattern1(nrows,ncols):
    ans,last=[],0
    for i in range(nrows):
        k=[]
        for j in range(last+1,(ncols*(i+1))+1):
            k.append(j)
            last=j
        ans.append(k)
    return ans
def pattern2(nrows,ncols):
    ans,last=[],0
    for i in range(nrows):
        k=[]
        for j in range(last+1,(ncols*nrows)+1,nrows):
            k.append(j)
        last+=1
        ans.append(k)
    return ans
def pattern3(N):
    ans,zero,j=[],0,1
    for i in range(1,N+1):
        k,count=[],1
        for r in range(zero):
                k.append(0)
                count+=1
        while count<=N:
            k.append(j)
            j+=1
            count+=1
        ans.append(k)
        zero+=1
    return ans
def pattern4(N):
    ans,zero,j,m=[],0,1,1
    for i in range(1,N+1):
        k,count,multiplier=[],1,0
        for r in range(zero):
                k.append(0)
                if count==1:multiplier+=2
                else:multiplier+=1
                count+=1
        while count<=N:
            k.append(j)
            if count==1:multiplier+=2
            else:multiplier+=1
            j+=multiplier
            count+=1
        ans.append(k)
        zero+=1
        if m<len(k):j=k[m]-1
        m+=1
    return ans
def pattern5(N):
    ans=[[0]*N for x in range(N)]
    s=1
    for i in range(N):
        for j in range(N-i):
            c=i+j
            ans[j][c]=s  
            s+=1
    return ans
def pattern6(N):
    ans=[[0]*N for x in range(N)]
    s=1
    for i in range(N):
        if i%2==0:
            for j in range(N-i):
                c=i+j
                ans[j][c]=s  
                s+=1
        else:
            for j in range(N-i-1,-1,-1):
                c=i+j
                ans[j][c]=s  
                s+=1
    return ans
exec(input().strip())