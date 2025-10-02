#profit = SP - CP  #if data is +ve then profit else loss means -ve

s_p = float(input("Enter the seeling price : "))
c_p = float(input("ENter the Cast price : "))
price = s_p - c_p

if price < 0:
    print('loss ')
elif price > 0:
    print('profit ')
else:
    print('no loss no profit')
