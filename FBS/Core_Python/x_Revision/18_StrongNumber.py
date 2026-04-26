num = int(input("Enter the number: "))

# temp = num
# sum = 0

# while(temp):
#     digit = temp%10
#     mul = 1
#     while(digit):
#         mul *= digit
#         digit -= 1
    
#     sum += mul
#     temp //= 10

# if sum == num:
#     print(f'the number is strong number : {num}')
# else:
#     print(f'the number is NOT strong number : {num}')

#1,2,145, 40585
# 145 = > 1!+4!+5! = 1+24+120 =145
temp = num
sum = 0
while(temp):
    digit = temp %10
    mul = 1
    for i in range(1, digit+1):
        mul *= i
    sum += mul
    temp //= 10

if sum == num:
    print(f'the number is strong number : {num}')
else:
    print(f'the number is NOT strong number : {num}')