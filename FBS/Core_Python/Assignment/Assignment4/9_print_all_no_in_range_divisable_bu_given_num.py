#print_all_no_in_range_divisable_by_given_number
num = int(input("Enter the number need to check division : "))
start, end = input("Enter the range until which i from to end check : ").split()
start = int(start)
end = int(end)

print(num, start, end)

temp = start

while(temp<=end):
    if(temp%num) == 0:
        print(temp)
    temp += 1
print('Complete')