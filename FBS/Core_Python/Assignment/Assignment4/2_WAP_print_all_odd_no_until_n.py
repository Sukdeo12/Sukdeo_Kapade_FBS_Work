# num = 11
# num/2 => Q -> 5 and Reminder -> 1 or not zero(odd) 

num = int(input("ENter the number : "))
# temp = 0
# print('The odd1 numbers are : ')
# while(num >= temp):
#     if ((temp % 2) != 0):
#         print(temp)
#     temp += 1

#using for loop
print("odd num within range is : ")
for i in range(1, num+1):
    if i%2 != 0 :
        print(i)
else:
    print('number updated successfully')