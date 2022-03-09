s = input("Enter a String: ")
middle = s.find(" ")
firsthalf = s[:middle]
secondhalf = s[middle+1:]
newstring = secondhalf + " " + firsthalf
print(newstring)