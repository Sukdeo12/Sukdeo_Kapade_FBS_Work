num = int(input("Enter the number: "))
act_num = num
rev =  0
cnt = 0
while(num):
    #print(num//10)
    rev *= 10
    rev += num%10
    
    print(num%10, rev)
    num //= 10
    cnt += 1
    
if act_num == rev:
    print(f'This is the pallundrom number {num}, cnt is {cnt}')
else:
    print(f'Not pallindrom number {num} and cnt is {cnt}')