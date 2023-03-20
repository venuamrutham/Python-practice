# Prime numbers between two ranges

a,b = input("Enter two numbers to define a range to print the prime numbers in between: ").split()

a,b = int(a),int(b)

prime_set = set()

if a > b:

    a,b = b,a

for i in range(a,b+1):

    for k in range(2,i):

        if i % k == 0:

            break

    else:

        prime_set.add(i)

        
if a == b or len(prime_set) == 0:

    print("No prime numbers in between")

else:
    
    print(sorted(prime_set))











