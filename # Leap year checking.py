# Leap year checking

a = int(input("Entera year to check it is leap year or not: "))

if a%4 == 0 and (a % 100 != 0 or a % 400 == 0):
    print("It is a leap year")
else:
    print("It is not a leap year")



