#Cal area of Traingle Tri_area = 1/2 * base * hight  and area_rectangel = length * width
b = 0
h = 0
b, h = input("Enter the triangle base and hight : " ).split()
b = float(b)
h = float(h)
#print("Given data are, base: ", base, "Hight: ", hight)
area_triangle = (b * h)*(0.5)
print("area of triangle is : ", area_triangle)
 
l=0
w=0
l,w = input("Enter the rectangle leght and widht : ").split()
l = float(l)
w = float(w)
area_rect = l*w
print("area of rectangle is : ", area_rect)