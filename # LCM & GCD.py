# LCM & GCD

import math

n = int(input("Enter how many numbers you want to enter to check LCM or GCD: "))

LCM_set = set()

for i in range(n):

    current_number = int(input("Enter number: "))

    LCM_set.add(current_number)

LCM_list = list(LCM_set)

check = int(input("Enter 1 for LCM and 2 for GCD and 3 for both LCM and GCD: "))

if check == 1:

    print(math.lcm(*LCM_list), " is lcm of numbers " )

elif check == 2:

    print(math.gcd(*LCM_list), " is gcd of numbers ")

elif check == 3:

    print(math.lcm(*LCM_list), " is lcm of numbers ")
    print(math.gcd(*LCM_list), " is gcd of numbers ")

else:

    print("Invalid entry")





