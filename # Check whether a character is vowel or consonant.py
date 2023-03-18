# Check whether a character is vowel or consonant

a = input("Enter a alphabet to check it is a vowel or consonant: ").lower()

if a.isalpha():

    if a in "aeiou":
        print("It is vowel")

    else:
        print("It is consonant")
else:
    print("Please enter a alphabet")












