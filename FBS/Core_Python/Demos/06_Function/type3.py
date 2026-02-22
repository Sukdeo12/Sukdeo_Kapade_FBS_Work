#without passing paramet 
#with returning value

def fact( ):
    num = int(input("Enter the number : "))
    facto = 1
    for i in range(1, num+1):
        facto = facto*i
    
    return 

print(f'Start the function -> ')
result = fact( )
print("result is : ", result)
if result is None:
    
    print('Result is ', type(result))
    