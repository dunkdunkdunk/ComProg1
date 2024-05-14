from collections import OrderedDict
def read_data(): # this function is given
    seqs = input().strip().split('\\n')
    return seqs
def get_frequency_matrix(dnas):
    check=[]
    A,T,C,G=[],[],[],[]
    for i in dnas:
        check.append(len(i))
    if len(set(check))>1:return "Found incorrect DNA length"
    for i in range(check[0]):
        l=OrderedDict([('A',0),('T',0),('C',0),('G',0)])
        for j in dnas:
            if j[i] in l.keys():
                l[j[i]]+=1
            else:return "Found incorrect nucleotide"
        ans=list(map(str,l.values()))
        A.append(ans[0]);T.append(ans[1]);C.append(ans[2]);G.append(ans[3])
    return ','.join(A)+'\n'+','.join(T)+'\n'+','.join(C)+'\n'+','.join(G)
def get_frequency_matrix_w_pc(dnas):
    l=get_frequency_matrix(dnas).split()
    if 'Found' in l: return ' '.join(l)
    ans=[]
    for i in l:
        p=list(map(int,i.split(',')))
        for j in range(len(p)):
            p[j]=str(p[j]+1)
        ans.append(','.join(p))
    return '\n'.join(ans)
cmd = input().strip().split('; ')
for c in cmd: exec(c)