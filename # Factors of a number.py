# Factors of a number

a = int(input("Enter a number to get factors of it: "))

factors = set()

for i in range(1,a+1):

        if a % i == 0:

            factors.add(i)

print(sorted(factors), " are list of factors")













