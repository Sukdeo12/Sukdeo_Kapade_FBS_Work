# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

l = 50
b= 40
r = b/2

actaul_area = 5*((2*l + 40) + (3.14*r))

total_field = actaul_area*35

print(f'total area is {actaul_area} and total field cast is {total_field}.')