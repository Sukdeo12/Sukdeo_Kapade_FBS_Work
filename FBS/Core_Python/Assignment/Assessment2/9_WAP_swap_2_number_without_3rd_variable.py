#num1 = 0, num2 = 0, num3 = 0
#num1, num2 = map(int, input("Enter the two input - ").split())  #if both are int
num1, num2 = input("Enter the two input - ").split()
num1, num2 = int(num1), float(num2)
# num3 = num1
# num1 = num2
# num2 = num3
num1, num2 = num2, num1  #creates a temporary tuple (num2, num1) and unpacks it back into num1 and num2

print("Swaping number are - num1 : ", num1, ", num2 : ", num2)