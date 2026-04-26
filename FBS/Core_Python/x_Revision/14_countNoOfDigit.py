num = int(input('Enter the number: '))
temp = num
cnt = 0
while(temp):
    cnt += 1
    temp //= 10
print(f'{num}  count is {cnt}')