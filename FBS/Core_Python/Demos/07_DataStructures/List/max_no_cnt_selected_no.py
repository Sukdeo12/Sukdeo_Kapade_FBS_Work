li = [10,20,45,2,5,99, 10, 38,17, 45, 99, 45]
cnt =0
num = int(input('Enter the num you wnat to find the count : '))
for el in li:
    if num == el:
        cnt += 1

print(f'The max no of cnt is = {cnt} of following given number {num}')    
print(f'List is {li}')