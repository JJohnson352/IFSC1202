s = input("Enter a String: ")
if s.count("f") == 1: 
    print(s.find("f"))
if s.count("f") >= 2:
    print(s.find("f"))
    print(s.rfind('f'))
if s.count('f') == 0:
    print(0)