N = int(input("Enter N: "))
sum = 0
for i in range(1,N+1):

    factorial = 1
    for j in range(1, i+1):
        factorial = factorial * j
        
    sum = sum + factorial
print(sum)