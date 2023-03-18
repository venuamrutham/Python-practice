# Find area of a rectangle
'''
a = float(input("please enter the length of rectangle ......."))

b = float(input("please enter the breadth of rectangle......."))

area = a*b

print("area_of_rectangle is ....... ", area)'''


def calculate_rectangle_area(length, width):
    area = length * width
    return area

length = float(input("Please enter the length of the rectangle: "))
width = float(input("Please enter the width of the rectangle: "))

area = calculate_rectangle_area(length, width)
print("The area of the rectangle is:", area)


