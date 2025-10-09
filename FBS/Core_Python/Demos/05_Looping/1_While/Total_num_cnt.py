
#Dry Runn..Assempted execution
# num = 1234
# num % 10 -> 4    cnt = 1   num // 10 -> 123    check num > 0 or while(num)
# num % 10 -> 3    cnt = 2   num // 10 -> 12
# num % 10 -> 2    cnt = 3   num // 10 -> 1
# num % 10 -> 1    cnt = 4   num // 10  -> 0

num = int(input("Enter the num: "))
temp = num
cnt = 0

while(temp):
    #temp  %= 10
    temp //= 10
    cnt += 1
    
print(f'number count is {cnt}')