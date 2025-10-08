#Men gose for shoppe, He buy 5 product, accept the price of all product. and dispaly the total bill after addijng 18% gst.

product1 = float(input("Enter the price of product 1: "))
product2 = float(input("Enter the price of product 2: "))
product3 = float(input("Enter the price of product 3: "))
product4 = float(input("Enter the price of product 4: "))
product5 = float(input("Enter the price of product 5: "))

price = product1 + product2 + product3 + product4 + product5
total_price = price + ((18/100)*price)

print(f'the total bill = {total_price}')