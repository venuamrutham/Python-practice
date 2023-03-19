# Prime numbers between two ranges


set_range = list(int(input("Enter two numbers to define a range to print the prime numbers in between: ")) for i in range(2))

set_range = sorted(set_range)

prime_set = set()

print(set_range)

for i in range(set_range[0],set_range[1]+1):

    for k in range(2,i):

        if i % k == 0:

            break

    else:

        prime_set.add(i)
            

print(sorted(prime_set))











