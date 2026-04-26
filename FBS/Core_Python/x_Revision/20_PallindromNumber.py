num = int(input('ENter the number : '))
temp = num
s = 0
while(temp):
    #print(temp%10)
    s *= 10
    s += temp%10
    temp //= 10

if s == num:
    print('Pallindrom ', s)
else:
    print(f'{num} not pallindrom')
