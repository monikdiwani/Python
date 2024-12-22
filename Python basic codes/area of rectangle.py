#WAP to get Area of Rectangle

def area(length, breadth):
    return length * breadth

length = int(input("Enter the length of the rectangle: "))
breadth = int(input("Enter the breadth of the rectangle: "))

result = area(length, breadth)
print("The area of the rectangle is:", result)
