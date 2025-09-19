# num1 = 10
# num2 = 20.5

num1 = (input('Enter Number 1 : '))
num2 = (input('Enter Number 2 : '))
print(num1 , type(num1))
print(num2 , type(num2))

sum = num1 + num2

print('addition is ', sum)   #print function takes multiple parameters

# #     #typecasting -> chaning type of one datatype to other data type

print('addition is ' + str(sum))   #Concatinate the string of number

#     #format is trying to chnage : {} it will gose the num value into string ->  to understand the veriable we can used { }
print(f'Addition of {num1} and {num2} is {sum}.')   #f String format

# #Second Method
# Now num1 and num2 creating as dynamic -. bacause no user interaction here : input()  -> help to take input form User

