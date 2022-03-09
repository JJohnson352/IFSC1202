s = input("Enter a String: ")
middle =((len(s)+1)//2)
firsthalf = s[:middle]
secondhalf = s[middle:]
newstring = secondhalf + firsthalf
print(newstring)