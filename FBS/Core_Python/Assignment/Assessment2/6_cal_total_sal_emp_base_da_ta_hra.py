#WAP to calculate total salary of empoyee based on DA = 10% of basic,  TA = 12% of basic and HRA=15% of basic
basic_price = input("ENter the basic sal : ")
basic_price = float(basic_price)
DA = (10/100)*basic_price
TA = (12/100)*basic_price
HRA = (15/100)*basic_price

total_Sal = basic_price + DA + TA + HRA

print("Total salary is :: ", total_Sal)