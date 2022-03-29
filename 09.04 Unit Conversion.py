fromvalue = 1
fromunit = "cm"
tounit = "mm"

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
    if a[0][i] == fromunit:
        fromindex = i
        break
print(fromindex)

# search 0th colimn for to value
for i in range(len(a)):
    if a[i][0] == tounit:
        toindex = i
        break
print(toindex)

conversion = float(a[fromindex][toindex])
print(conversion)
tovalue = fromvalue * conversion
print(tovalue)

