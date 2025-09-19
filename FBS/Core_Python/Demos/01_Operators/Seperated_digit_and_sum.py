num = int(input("Enter 3 digit number : "))

num = int(num)

d1 = num%10
num = num//10

d2 = num%10
num = num//10

d3 = num%10
num = num//10

sum = d1 + d2 + d3

print(f' seperate digit d1 : {d1}, d2 : {d2}, d3 : {d3}. Some for digits are : {sum}')