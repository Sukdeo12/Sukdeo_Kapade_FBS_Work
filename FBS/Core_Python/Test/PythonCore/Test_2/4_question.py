#Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

# area of wall is Aw = side *side

size_of_internal_wall = float(input("Enter the size of wall: "))
area_of_internal_wall = size_of_internal_wall * size_of_internal_wall
cast_of_interiar_penting = float(input("Enter the  cast of interior peint: "))
Total_interior_cast = 4 * cast_of_interiar_penting * area_of_internal_wall

print(f'Total interior cast of penting is : {Total_interior_cast}')