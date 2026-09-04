def calculate_area(length, width):
    area = length * width
    return area

def calculate_perimeter(length, width):
    perimeter = 2 * (length + width)
    return perimeter

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))

area = calculate_area(length, width)
perimeter = calculate_perimeter(length, width)

print(f"The area of rectangle is {area}")
print(f"The perimeter of rectangle is {perimeter}")
