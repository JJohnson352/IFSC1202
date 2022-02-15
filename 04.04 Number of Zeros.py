N = int(input("Enter N: "))
counter = 0
for i in range(1,N+1):
    number = int(input("Enter Number: "))
    if (number == 0):
        counter = counter + 1
print(counter)