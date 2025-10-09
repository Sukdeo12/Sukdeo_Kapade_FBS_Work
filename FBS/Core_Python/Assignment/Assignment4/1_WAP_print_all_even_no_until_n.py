# num = 12
# 12/2 = 6 (Quetient) and reminder = 0 if reminder == 0 then number is even number


num = int(input("Enter the number: "))
temp = 0
print('The even numbers are : ')
while(temp <= num):
    if temp % 2 == 0:
        print(temp)    
    # else:
    #     print(f'number {temp}, is odd number')
    temp += 1