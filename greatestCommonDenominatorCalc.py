a=int(input("Enter a value for a "))
b=int(input("Enter a value for b "))

#calc GCD
while b!=0:
	print (a,b)
	(a,b)=(b,a%b)
print("The GCD of the two values is: "+str(a))
