# num = int(input('Enter the number to check if prime or not : '))
# for i in range(2,num):
#     print(i)
#     if(num%i == 0):
#         print(f'{num} is not prime number')
#         break
# else:
#     print(f'{num} is prime number')


#List of prime num
li = []
num = int(input('Enter the number :'))
print('List the prime number until number ', num,' are : ')


for i in range(2,num+1):
      
    for j in range(2, i):
        if (i%j == 0):
            break
    else:
        #print(i)
        li.append(i)

print(li)        
    
    