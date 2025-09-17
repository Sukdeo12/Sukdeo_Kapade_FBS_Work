act_price = input("Enter the actual price of the book : ")
act_price = float(act_price)
discount = input("Please enter discount on book (%): ")
discount = float(discount)
#selling Price = Market_price *(100-Discount%)/100
sell_price = act_price * ((100-discount)/100)
print("Selling price is : ", sell_price)