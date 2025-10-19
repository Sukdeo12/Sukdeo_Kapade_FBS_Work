num = int(input('Enter the number to check if number perfect or not(e.g 28): '))
# temp = 1
# sum = 0

# while(temp <= num): #loop1
#     i = 1
#     while(i < num):
#         if (temp * i) == num:
#             sum += i
#             # print('temp : ', temp)
#             # print('i : ', i)
#         i += 1
        
#     temp += 1
# print('sum = ', sum)
# if(sum == num ):
#     print("Number is the perfect number : ", num)
# else:
#     print("Number is the NOT perfect number : ", num)
    
# print('Complete')
sum = 0
for i in range(1, num+1):
    for j in range(1, num):
        if (i*j) == num:
            sum += j
print('sum = ', sum)
if(sum == num ):
    print("Number is the perfect number : ", num)
else:
    print("Number is the NOT perfect number : ", num)
    

