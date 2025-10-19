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