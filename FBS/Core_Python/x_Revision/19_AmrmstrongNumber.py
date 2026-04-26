#Armstrong number or narcissistic numbers
# Single-digit Armstrong numbers: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

# 3-digit Armstrong numbers: 153, 370, 371, 407

# 4-digit Armstrong numbers: 1634, 8208, 9474

# 5-digit Armstrong numbers: 54748, 92727, 93084

# 6-digit Armstrong number: 548834

start_num, end_num = input("Enter the range of (start and end number : ").split()

start_num = int(start_num)
end_num = int(end_num)

num = start_num

while(num<=end_num):
    temp = num
    sum = 0
    digit = 0
    #check the number of digit 
    while(temp ):
        digit += 1
        temp //= 10

    # print('The numbe of digits are: ',digit)

    temp = num
    while(temp):
        sum += (temp%10) ** digit
        temp //= 10

    if sum == num:    
        print(f'sum = {sum}, num = {num} is armstrong number')        
    # else:
    #     print(f'sum = {sum}, num = {num} is NOT armstrong number')  
    num += 1   