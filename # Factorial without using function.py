# Factorial without using function

"""a = int(input("Please enter a number to find factorial: "))

factorial = 1

for i in range(1,a+1):

    factorial = i*factorial

print("Factorial of your entered values is ",factorial) """

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

a = int(input("Please enter a number to find factorial: "))

result = factorial(a)

print("Factorial of", a, "is", result)









