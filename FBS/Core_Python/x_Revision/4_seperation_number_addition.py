#Num = 456
#4 + 5 + 6 = 15

num = 456
temp = num
add = 0
rem = 0

print(f'-> {temp} Sum of {num} is : {add}')
rem = num % 10
num = num // 10
add = add + rem
print(f'-> {temp} Sum of {num} is : {add}')

rem = num % 10
num = num // 10
add = add + rem
print(f'-> {temp} Sum of {num} is : {add}')

rem = num % 10
num = num // 10
add = add + rem
print(f'-> for {temp} - Sum of {num} is : {add}')


