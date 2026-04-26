import random
user = 'Sukdeo'
password = 'oedkus'

print('*** TO LOGIN INTO ACCOUNT *** ')
usr = input('Enter the userid : ')
if usr == user:
    psw = input('Enter the password : ')
    if psw == password:

        captcha = random.randint(11111,99999)
        print(f'Your CATPCHA is :: {captcha}')
        ca = int(input('Please enter the capta to verify:'))

        if captcha == ca:
            print(f'Hello {user}, you login successfully. ')
    else:
        print(f'Your passowrd is incorrect.')
else:
    print(f'Your User Id is incorrect.')        

