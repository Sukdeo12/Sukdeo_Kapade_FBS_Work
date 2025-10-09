# num = 5!
# 5*4*3*2*1 = ans 

num = int(input("Enter the number: "))
temp = num
mul = 1
while(temp>0):
    mul *= temp
    temp -= 1
    
print(f'factorial of {num} is: {mul}.')
    