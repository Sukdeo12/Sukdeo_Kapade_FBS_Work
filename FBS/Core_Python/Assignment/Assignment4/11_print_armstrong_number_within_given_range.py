#Armstrong number
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
