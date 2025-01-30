#Lab 2 Program 1
#Classifies triangles
Side1=float(input("Side length 1: "))
Side2=float(input("Side length 2: "))
Side3=float(input("Side length 3: "))
if Side1==Side2:
    if Side1==Side3:
        print("This is an equilateral triangle!")
    else:
        print("This is an isosceles triangle!")
elif Side2==Side3 or Side1==Side3:
    print("This is an isosceles triangle!")
else:
    print("This is a scalene triangle!")