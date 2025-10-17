data = int(input("Enter the name: "))
num1 = 0
num2 = 1
res = 0

while(data >= res ):
    if num1 == 0 and res == 0:
        print(num1)
        res = num1
        if num1 == data:
            break
        
    if num2 == 1 and res == 1:
        print(num2)
        res = num2
        if num2 == data:
            break      
    if res:
        print(res)     
           
    res = num1 + num2
    num1 = num2
    num2 = res
        