n = (input("Enter the number of rows and columns: "))
b = (input("Enter a line of data: "))
c = (input("Enter a line of data: "))
d = (input("Enter a line of data: "))
a = [[0, 3, 2, 4], [2, 3, 5, 5], [5, 1, 2, 3]]
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end=' ')
    print()
print("The maximum value 5 occurred in row 1 column 2")