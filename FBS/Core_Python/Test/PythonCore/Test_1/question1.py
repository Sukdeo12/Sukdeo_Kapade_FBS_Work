# WAP to fid area of parameter of following figuer(accept length, breath, and radius)
#Inputs are : len, bre, r = bre/2

len = float(input("Enter the length of the semi cirecle rectanagle - "))
bre = float(input("Enter the breath of the semi cirecle rectanagle - "))
red = bre/2

#print (f'Lenth is {len} and Breath is {bre}.')

#Area = area of reactangle + area of semicircle

area_rectangle = len*bre
area_semicirecle = 3.14 * red
#Total area calcukated
area = area_rectangle + area_semicirecle

#Peremeter = Peemeter of rectangle + circumference of semicirecle
peri_rectangle = 2*len + bre
circumfernce_semiirecle = (3.14 + red)

peri = peri_rectangle + circumfernce_semiirecle

print(f'Total area of semicirecle rectangel is {area} and perimeter id {peri}')