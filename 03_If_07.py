a = input()
if len(a) > 10 : print(str((int(a)/1000000000)+1).split(".")[0]+"B" if int(str(round(int(a)/1000000000,1)).split('.')[-1]) > 5 or int(str(round(int(a)/1000000000,1)).split('.')[-1]) == 0 else (str(int(a)/1000000000).split("."))[0]+"B")
elif len(a) == 10 : print(str(round(int(a)/1000000000,1))+"B")

elif len(a) > 7 and len(a) < 10 : print(str((int(a)/1000000)+1).split(".")[0]+"M" if int(str(round(int(a)/1000000,1)).split('.')[-1]) > 5 or int(str(round(int(a)/1000000,1)).split('.')[-1]) == 0 else (str(int(a)/1000000).split("."))[0]+"M")
elif len(a) == 7 : print(str(round(int(a)/1000000,1))+"M")

elif len(a) > 4 and len(a) < 7 : print(str((int(a)/1000)+1).split(".")[0]+"K" if int(str(round(int(a)/1000,1)).split('.')[-1]) > 5 or int(str(round(int(a)/1000,1)).split('.')[-1]) == 0 else (str(int(a)/1000).split("."))[0]+"K")
elif len(a) == 4 : print(str(round(int(a)/1000,1))+"K")

else: print(a)