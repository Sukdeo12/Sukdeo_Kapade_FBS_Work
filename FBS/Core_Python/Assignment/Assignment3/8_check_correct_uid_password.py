import random
uid = "sukdeo"
password = "Sukdeo@123"

user = input("Enter the user uid : ")
pswd = input("Enter the password : ")

if ((uid == user) and (pswd == password)):
    print("uid and password is correct")
    
    #Crete captcha
    
    captcha = random.randint(0000,9999)
    
    print('your captcha is :', captcha)
    c = int(input("enter the captch: "))

    if c == captcha:
        print('Login succesfull...!')
    else:
        print("captcha is wrong,please login again")
else:
    print("uid and password is incorrect")



