#WAP to calculate tolal cast of Interior and exteria Area of building'
#KNow data is Aw = Area of wall, Ce = Exterior cast, Ci = Interior cast

Ai = float(input("Enter the Area of the wall (considering internal Ai) : "))
Ae = float(input("Enter the Area of the wall (considering external Ae) : "))
Ci = float(input("enter the cast of interior paint Ci: "))
Ce = float(input("enter the cast of exterion paint Ce: "))

#Total Interior cast TCi = 8*Aw*Ci
#Total Exterior cast TCe = 7*Ae*Ce

TCi = 8*Ai*Ci
TCe = 7*Ae*Ce

TC = TCi + TCe

print(f'Total cast of the paint is : {TC}.')