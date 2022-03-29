a = "1 20 30 3 40 50 9 11 "
b = a.split()
for i in range(len(b)):
    b[i] = int(b[i])
for i in range(len(b)):
    print(b[i])