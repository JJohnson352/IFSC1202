n = (int(input("Enter from Value: ")))
b = (input("Enter From Unit (mm, cm, m, km, in, yd, mi): "))
c = (input("Enter To Unit (mm, cm, m, km, in, yd, mi): "))

fromvalue = n

a = []
numbersfile = open("09.04 Conversion.txt")
x = numbersfile.readline()
while x != "":
	y = x.split()
	a.append(y)
	x = numbersfile.readline()
numbersfile.close()

fromindex = 0
toindex = 0

# search 0th row for from value
for i in range(len(a[0])):
    if a[0][i] == b:
        fromindex = i
        break
print(fromindex)

# search 0th colimn for to value
for i in range(len(a)):
    if a[i][0] == c:
        toindex = i
        break
print(toindex)

conversion = float(a[fromindex][toindex])
print(conversion)
tovalue = fromvalue * conversion
print(tovalue)

