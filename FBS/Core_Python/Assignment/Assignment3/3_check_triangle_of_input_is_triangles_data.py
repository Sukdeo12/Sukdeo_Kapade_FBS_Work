#input is 3-traingles 
#if addition of 3 tringle = 180then it's valied else not valied

angle1 = float(input("Enter the triangle angle 1: "))
angle2 = float(input("Enter the triangle angle 2: "))
angle3 = float(input("Enter the triangle angle 3: "))

angles = angle1 + angle2 + angle3

if angles == 180:
    print("triangle is valid ", angles)
else:
    print("Triangle is invalied", angles)

