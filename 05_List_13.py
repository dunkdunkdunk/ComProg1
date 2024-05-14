a,_=[],input()
while _!='-1':a+=_.split();_=input()
print([int(i) for i in a[2::2][-1::-1]+a[1:len(a):2]])