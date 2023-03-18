# Fibonacci starting from any two numbers

a = int(input("Enter a first number to generate the fibonacci numbers: "))

b = int(input("Enter a second number to generate the fibonacci numbers: "))

n = int(input("Enter how many fibonacci numbers you want: "))

fibonacci_number = 0

if a < b:

        if n == 1:
            
            print(a)

        elif n == 2:

            print(a,b) 
        else:

            print(a)

            print(b)

            for i in range(3,n+1):

                fibonacci_number = a + b

                print(fibonacci_number)

                a = b

                b = fibonacci_number
            
else:

    print("Cannot generate the fibonacci numbers while first numbers is greater or equals to second number.")









