data = int(input('Enter the number : '))
li = []
for num in range(1,data + 1):
    for i in range(2,num):
        if num%i == 0:
            #print('Given num is not prime')
            break
    else:
        li.append(num)
        
print(f'prime number list is : {li}')