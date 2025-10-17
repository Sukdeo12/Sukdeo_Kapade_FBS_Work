num = int(input('Enter the number: '))
   
if num <= 1:
    print(f'{num} is not prime number')
else:
    temp  = num
    flag = 0
    i = 2
    while (i <= num**(1/2) ):
        if temp%i == 0:
            print(f'{num} is not prime number ')
            flag = 1
            break
        
        i += 1
        
    if flag==0:
        print(f'{num} is prime number ')