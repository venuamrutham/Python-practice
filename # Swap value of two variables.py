
# Swap value of two variables
'''
a = int(input("Enter the first number to perform swap: "))

b = int(input("Enter the second number to perform swap: "))

k = 1;

print("The numbers before swapping",a,b)

k = b

b = a

a = k

print("The numbers after swap", a,b)'''

a = int(input("Enter the first number to perform swap: "))

b = int(input("Enter the second number to perform swap: "))

print("The numbers before swapping",a,b)

a,b = b,a

print("The numbers after swap", a,b)

















