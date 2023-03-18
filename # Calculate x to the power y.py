# Calculate x to the power y

a = int(input("Enter the base: "))

b = int(input("enter the power: "))

exponentiation = 1

for i in range(1,b+1):
    exponentiation = exponentiation*a

    
if b == 0 and a != 0:
    
    print("Exponentiation is 1")

elif b == 0 and a == 0:

    print("Undefined")
    
else:
    print(exponentiation, "is exponentiation")

"""
a = int(input("Enter the base: "))

b = int(input("enter the power: "))

if a == 0 and b == 0:

    exponentiation = 0

else:

    exponentiation = a ** b

print(exponentiation, "is exponentiation")"""





