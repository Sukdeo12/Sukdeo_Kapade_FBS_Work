data = int(input('Enter the number till fabinacci series want to check: '))
a,b = 0,1
li = []
while(a <= data):
    #print(a)
    li.append(a)
    a,b = b, a+b
print(f'Fabinacci series till {data} is : {li}.')
sum = 0
for i in li:
    sum += i
print(f'total sum is : {sum}')