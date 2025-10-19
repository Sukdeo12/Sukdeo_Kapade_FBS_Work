num = int(input("Enter the number: "))

temp = num
sum = 0

while(temp):
    digit = temp%10
    mul = 1
    while(digit):
        mul *= digit
        digit -= 1
    
    sum += mul
    temp //= 10

if sum == num:
    print(f'the number is strong number : {num}')
else:
    print(f'the number is NOT strong number : {num}')
#print(f'sum = {sum}, num = {num}')