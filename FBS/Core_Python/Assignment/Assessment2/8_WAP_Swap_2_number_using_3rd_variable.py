#num1 = 0, num2 = 0, num3 = 0
#num1, num2 = map(int, input("Enter the two input - ").split())  #if both are int
num1, num2 = input("Enter the two input - ").split()
num1, num2 = int(num1), float(num2)
num3 = num1
num1 = num2
num2 = num3

print("Swaping number are - num1 : ", num1, ", num2 : ", num3)

#Below method we can use if data is variii
# user_input = input("Enter one or two numbers separated by space: ").split()

# if len(user_input) == 1:
#     num1 = float(user_input[0])
#     num2 = None  # or assign a default value like 0.0
#     print("Only one number entered.")
# elif len(user_input) == 2:
#     num1, num2 = map(float, user_input)
#     # Swap without third variable
#     num1, num2 = num2, num1
#     print("Swapped numbers are - num1:", num1, "num2:", num2)
# else:
#     print("Invalid input. Please enter one or two numbers.")