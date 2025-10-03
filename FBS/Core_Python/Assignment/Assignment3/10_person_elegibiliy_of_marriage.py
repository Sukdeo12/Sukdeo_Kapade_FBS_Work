print("Check if your eligibe for married or not")
print("Select the gender : ")
#print("1. Male")
#print("2. Female")

print("M -> Male")
print("F ->  Female")
#gender = int(input("Enter the gender: "))
gender = input("Enter the gender: ")

#if gender < 1 or gender > 2:
if not((gender == 'M') or (gender == 'F')):

    print("Your selected wrong gender")
    pass

else:
    age= int(input("Enter the age: "))
   # if gender == 1:
    if gender =='M':
        if age >= 21:
            print(f'your are Male, and your age is {age}, you are eligible for married')
        else:
            print(f'your are Male, and your age is {age}, you are NOT eligible for married')
    #if gender == 2:
    if gender == 'F':
        if age >= 18:
            print(f'your are female, and your age is {age}, you are eligible for married')
        else:
            print(f'your are female, and your age is {age}, you are NOT eligible for married')
