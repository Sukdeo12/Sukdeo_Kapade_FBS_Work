num = int(input('Enter the number : ')) 
Li =[]
temp = 1
while(temp <= num):
    for i in range(1,11):
        Li.append(i*temp)
    temp += 1

print(Li)
