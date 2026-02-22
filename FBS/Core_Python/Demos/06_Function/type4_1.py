#with passing the value
#with return the values

#check the perfect numbers  -> Addition of factors is same as number

def check_perfect_no(num):
    sum = 0
    print(hex(id(sum)))
    for i in range(1,num):
        
        if(num % i) == 0:
            sum += i
    return sum == num

num = int(input("Enter the number - "))
print(hex(id(num)))
if(check_perfect_no(num)):
    print(f'{num} is perfect number')
    
else:
    print(f'{num} is NOT perfect number')