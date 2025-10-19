num = int(input("ENter the number until we are checkng the data : (divisable by 2 and 3) : "))
temp = 1
# print("Numbers aren't divisable by 2 : ")
# while(temp <= num ):
#     #checking if the data is divisable by zero or not
#     if (temp % 2):
#        print(temp)
#     temp += 1
    
# print('--------------')
# temp = 1
# print("Numbers aren't divisable by 3: ")
# while(temp <= num ):
#     #checking if the data is divisable by zero or not
#     if (temp % 3 ):
#        print(temp)
#     temp += 1
    
# print("complete")

print("Numbers aren't divisable by 2: ")
for i in range(1, num+1):
    if i%2:
        print(i)
print("Numbers aren't divisable by 3: ")
for i in range(1, num+1):
    if i%3:
        print(i)