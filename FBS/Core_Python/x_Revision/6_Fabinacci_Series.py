data = int(input('ENter the data until want to print febinnaci no : '))
a,b = 0,1

while a <= data: 
    # print(a )
    if a == data:
        print(f'{data} this is fabinocci number.')
        break
    a, b = b, a+b
else:
    print(f'{data} this is NOT fabinocci number.')