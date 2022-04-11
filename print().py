print()
print("Example 5")
a = "1 2 3"
b = a.split()
for i in range(len(b)):
	b[i] = int(b[i])
for i in range(len(b)):
	print(b[i])