annualReturn=float(input("Enter an annual return value: "))
newReturn=annualReturn
immediate=650000
yearly=0

for i in range(0,20):
	yearly=yearly*annualReturn +50000
	if i>0:
		newReturn=newReturn*annualReturn
	print(yearly)
	print(newReturn)

print("Receiving the money today results in: "+str(newReturn*650000))
print("Receiving the yearly payment results in: "+str(yearly))
