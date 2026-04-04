li = [10,20,45,2,5,99, 10, 38]
min_num = li[0]
for el in li:
    if min_num > el:
        min_num = el

print(f'The max no in list is : {min_num}')    
print(f'List is {li}')