digit = int(input("Enter 3 digit number: "))
act_digit = digit

d3 = digit%10
digit = digit//10

d2 = digit%10
digit = digit//10

d1 = digit%10
digit = digit//10

print(d1, d2, d3)

if ((d1 == 2*d2) and (d1 == d3/2)):
    print('Yes, you have done it')
else:
    print('please try next time')