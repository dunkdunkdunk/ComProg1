a = (input()[1:-1].split(","))
b = (input()[1:-1].split(","))
print("["+str(float(a[0]))+",",str(float(a[1]))+",",str(float(a[2]))+"]","+","["+str(float(b[0]))+",",str(float(b[1]))+",",str(float(b[2]))+"]","=","["+str(float(a[0])+float(b[0]))+",",str(float(a[1])+float(b[1]))+",",str(float(a[2])+float(b[2]))+"]")