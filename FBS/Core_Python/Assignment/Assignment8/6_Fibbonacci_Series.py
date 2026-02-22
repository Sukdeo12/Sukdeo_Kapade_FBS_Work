#Pallindrom number

def reverse_numbers(num):
    var = num
    rem = 0
    sum = 0
    while(var != 0):
        rem = var % 10
        var = var // 10
        
        sum = sum*10 + rem
        
    print(f'{num} is reverse = {sum}')
        
    return sum == num 

num = int(input('Enter the number :'))

res = reverse_numbers(num)

if res:
    print(f'{num} is pallindrom number')
else:
    print(f'{num} is NOT pallindrom number')