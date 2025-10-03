#12. Write a program to check if given 3 digit number is a palindrome or not.
#12321 = 12321 i.e forward num == revierse number

num = int(input("Enter the number (accept 5 digit): "))
act_num = num
rev_num = 0

print(f'num = {num}')
if(num):
    rev_num *= 10
    rev_num = num%10
    num //= 10
    print(f'rev_num = {rev_num}')
    print(f'num = {num}')

if(num):
    rev_num *= 10
    rev_num += num%10
    num //= 10
    print(f'rev_num = {rev_num}')
    print(f'num = {num}')

if(num):
    rev_num *= 10
    rev_num += num%10
    num //= 10
    print(f'rev_num = {rev_num}')
    print(f'num = {num}')

if(num):
    rev_num *= 10
    rev_num += num%10
    num //= 10
    print(f'rev_num = {rev_num}')
    print(f'num = {num}')

if(num):
    rev_num *= 10
    rev_num += num%10
    num //= 10
    print(f'rev_num = {rev_num}')
    print(f'num = {num}')

if act_num == rev_num:
    print(f"Number is pallindrom number : {act_num}")
else:
    print(f"Number is NOT-pallindrom number : {act_num}")