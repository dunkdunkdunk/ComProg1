def reverse(d):
    ans={}
    for i,j in d.items():
        ans[j]=i
    return ans
def keys(d,v):
    ans=[]
    for i,j in d.items():
        if j==v:
            ans.append(i)
    return ans
exec(input().strip())