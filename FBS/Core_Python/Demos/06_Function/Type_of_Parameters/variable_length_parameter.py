#passing dynamic multiple number of parameter
def add(*num):          #Arguments
    #print(type(num))
    for i in num:
        print(i)
    
    #pass


add(10, 20, 30)
print('\n')
add(40, 45, 50, 60, 65)
print('\n')
add(40, 50, 'sukdeo', 22.3)