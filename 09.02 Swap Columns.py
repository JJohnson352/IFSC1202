def swap_columns(a, i, j):
	for k in range(len(a)):
		a[k][i], a[k][j] = a[k][j], a[k][i]

def print_list(b):
	for i in range(len(b)):
		for j in range(len(b[i])):
			print(b[i][j], end=' ')
		print()
	print()

a = []
numbersfile = open("09.02 NumbersList.txt")
x = numbersfile.readline()
while x != "":
	y = x.split(" ")
	for i in range(len(y)):
		y[i] = int(y[i])
	a.append(y)
	x = numbersfile.readline()

print_list(a)

i = 1
j = 4

swap_columns(a, i, j)
print_list(a)
