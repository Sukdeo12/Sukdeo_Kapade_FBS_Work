num = int(input("Enter the num: "))
end_num = int(input("ENter the end number"))

while(num<=end_num):
    print('Multiplication of :', num)
    for i in range(num, num*10+1, num):
        print(i, end=' ')
    num += 1
    