a = input()
print("Mobile number" if a[:2] in ["06","08","09"] and len(a) == 10 else "Not a mobile number")