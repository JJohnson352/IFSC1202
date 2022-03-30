a = []
numbersfile = open("CarSales.txt ")
x = numbersfile.readline()
while x != "":
	y = x.split()
	a.append(y)
	x = numbersfile.readline()
numbersfile.close()