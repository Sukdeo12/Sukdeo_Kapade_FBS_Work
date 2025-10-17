num = int(input("ENter the num (range check divisible by 7 and mutiple by 5): "))

temp =1

print("Check th list of number divisable by 7: ")

while(temp <= num):
    if (temp % 7) == 0:
        print(temp)
    temp += 1
    
print("Check the list multiple of 5 in given range: ")

temp = 1

while(temp<=num):
    if (temp % 5) == 0:
        print(temp)
    temp += 1
        
print('Complete')