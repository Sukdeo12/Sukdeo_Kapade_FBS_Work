checkPerfectNo = int(input('Enter the number (to check is this number is perfect or not?) : '))
sum = 0

# for i in range(1, checkPerfectNo+1):
#     for j in range(1,checkPerfectNo):
#         if i*j == checkPerfectNo:
#             sum += j
# if sum == checkPerfectNo:
#     print(f'{checkPerfectNo} is perfect number.')            
# else:
#     print(f'{checkPerfectNo} is NOT perfect number.')
    
#List the perfect numver until given number
print('List of perfect numbers are :')
li = []

sum = None
for i in range(1,checkPerfectNo+1):
    sum = 0
    for j in range(1, i+1):
        for k in range(1, i):
            if j*k == i:
                sum += k
    
    if sum == i:
        print(f'{i} is perfect Number')
        li.append(i)
    # else:
    #     print(f'{i} is NOT perfecr Number.')
        
#print(f'The perfect number list until this number {checkPerfectNo} is :: ', li)
print(li)
        
