n = input()
i = str(int(n[3]+n[10]+n[17]+n[24]+n[31]) + int(n[7]+n[12]+n[17]+n[22]+n[27]) + 10000)[-4:-1]
print(i+["A","B","C","D","E","F","G","H","I","J"][int(str(int(i[0])+int(i[1])+int(i[2]))[-1])])