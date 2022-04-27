class House ():
	
	def __init__(self, Address=" ", Sqft=" ", Price=" "):

		self.Address = Address
		self.Sqft = Sqft
		self.Price = Price

	def costpersqft(self):
		costpersqft =  self.price / self.Sqft
		return costpersqft


	def payment(self, ar, ny):
		
		return 100
        
def print_houselist(houselist):
	print("{:>14s}{:>14s}{:>14s}{:>14s}".format("Address", "Sqft", "Sqft Cost", "Price", "Payment"))
	for i in range(len(houselist)):
		print ("{:>14s}{:14.2f}{:14.2f}{:14.2f}".format(houselist[i].Address, houselist[i].Sqft, houselist[i].Price, houselist[i].Payment()))


def find_house(houselist, housetofind):
	for i in range(len(houselist)):
		if houselist[i].Address == housetofind:
			return i
	return -1		

ny = input('Enter Interest Rate: ')
ar = input('Enter Years of Morgage: ')

houselist = []

housefile = open("Exam Three Houses.txt")

x = housefile.readline()



while x != "":
	print(x) 
	y = x.split(",")
	print(y) 
	myhouse = House()
	myhouse.Address = y[0].strip()
	myhouse.Sqft = float(y[1].strip())
	myhouse.Price = float(y[2].strip())
	houselist.append(myhouse)
	x = housefile.readline()

housefile.close()

print_houselist(houselist)
