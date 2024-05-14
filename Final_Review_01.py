def get_consensus(ss):
    ss=[i.upper() for i in ss.split('\n')]
    consensus=[]
    for i in range(len(ss[0])):
        num=[]
        for j in ss:
            num.append(j[i])
        count=dict()
        for k in num:
            if k in count.keys():
                count[k]+=1
            else: count[k]=1
        m=max(count.values())
        ans=[]
        for n in count:
            if count[n]==m:ans.append(n)
        ans.sort()
        consensus.append('/'.join(ans))
    consensus=' '.join(consensus)
    return consensus # DO NOT MODIFY THIS LINE
def get_consensus_generic(ss):
    ss,sl=[i.upper() for i in ss.split('\n')],max(len(i) for i in ss.split('\n'))
    for i in range(len(ss)):
        if len(ss[i])<sl:
            ss[i]=ss[i]+'0'*(sl-len(ss[i]))
    consensus=[]
    for i in range(len(ss[0])):
        num=[]
        for j in ss:
            num.append(j[i])
        count=dict()
        for k in num:
            if k in count.keys():
                count[k]+=1
            else: count[k]=1
        m=max(count.values())
        ans=[]
        for n in count:
            if count[n]==m:ans.append(n)
        ans.sort()
        consensus.append('/'.join(ans))
    consensus=' '.join(consensus)
    return consensus # DO NOT MODIFY THIS LINE

# exec(input().strip())
ss = ("YCXBATGZ\n" +
"YCVBaCGZ\n" +
"ACXBCTGZ\n" +
"CtCAATTZ\n" +
"CTXAATTM")
print('C/Y C X B A T G Z'==get_consensus_generic(ss))
ss = ("YCXBATGZ\n" +
"YCVBaCGZHQ\n" +
"ACXBCTGZHQ\n" +
"CtCAATTZHD\n" +
"CTXAATTMFD")
print('C/Y C X B A T G Z H D/Q'==get_consensus_generic(ss))
ss = ("YCXBATGZ\n" +
"YCVCaCGZHQ\n" +
"ACXDCTGZHQ\n" +
"CtCTATTZHD\n" +
"CTXAATTMFD")
print('C/Y C X A/B/C/D/T A T G Z H D/Q'==get_consensus_generic(ss))