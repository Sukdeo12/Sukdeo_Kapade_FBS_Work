#num = 5
# 5+4+3+2+1 = 15

num = int(input("Enter the number: "))
# temp = num
# sum = 0
# while(temp>0):
#     sum += temp
#     temp -= 1
    
# print(f'sum of the  series is: {sum}.')

#using for loop
sum = 0    
for i in range (num+1):
    sum += i
print(f'sum of the  series is: {sum}.')

