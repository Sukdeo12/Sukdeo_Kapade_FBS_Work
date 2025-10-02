a = float(input("Enter the side 1 (a): "))
b = float(input("Enter the side 2 (b): "))
c = float(input("Enter the side 3 (c): "))

if ( (a + b > c) and (b + c > a) and (a + c > b)):
    print('tringle is valid')
else:
    print('tringle is invalid')
