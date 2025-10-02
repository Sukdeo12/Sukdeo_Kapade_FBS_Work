#input is 3-traingles 
#if addition of 3 tringle = 180then it's valied else not valied

angle1 = float(input("Enter the triangle angle 1: "))
angle2 = float(input("Enter the triangle angle 2: "))
angle3 = float(input("Enter the triangle angle 3: "))

angles = angle1 + angle2 + angle3

if angles == 180:
    print("triangle is valid ", angles)
        
    if angle1 == angle2 == angle3 == 60:
        print("Qeuilateral Tringle")
    if ((angle1 != angle2) and (angle2 != angle3) and (angle3 != angle1)):
        print("scalen triangle")
    if ((angle1 == angle2 != angle3) or (angle2 == angle3 != angle1) or (angle3 == angle1 != angle2)):
        print("Isoscale trainge")

else:
    print("Triangle is invalied", angles)

