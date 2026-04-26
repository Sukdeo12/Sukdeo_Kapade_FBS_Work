Gender = input('Enter the Gender (Male-M/Female-F) : ')

if Gender == 'M' or Gender == 'F':
    Age = int(input('Enter the age : '))
    if Age > 0:
        if Gender == 'M':
            if Age >= 21:
                print('Your eligible for married')
            else:
                print('Sorry your Not eligible for married (Age must be 21+ )')
        if Gender == 'F':
            if Age >= 18:
                print('Your eligible for married')
            else:
                print('Sorry your Not eligible for married (Age must be 18+ )')    
    else:
        print('Please enter the valid Age')
    
else:
    print('Please ENter the Valid Gender M/F ')
