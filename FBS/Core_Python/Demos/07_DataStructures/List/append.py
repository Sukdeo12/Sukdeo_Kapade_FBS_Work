# li = []
# print(li)
# li.append(40)
# print(li)
# li.append(None)
# print(li)
# li.append(50)
# print(li)

#Create program to find max no in list
li = [10,20,45,2,5,99, 10, 38]
max_num = 0
for el in li:
    if max_num < el:
        max_num = el

print(f'The max no in list is : {max_num}')    
print(f'List is {li}')