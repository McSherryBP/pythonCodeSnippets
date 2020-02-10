a=int(input("Enter a value for a "))
b=int(input("Enter a value for b "))
temp=0
#calc GCD
while b!=0:
    temp=a
    a=b
    b=temp%b
print("The GCD of the two values is: "+str(a))
