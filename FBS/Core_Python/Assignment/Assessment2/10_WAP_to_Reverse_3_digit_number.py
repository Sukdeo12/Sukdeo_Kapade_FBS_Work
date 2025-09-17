num = input("Enter the 3 digit Number : ")
num = int(num)

rev_num = 0
rev_num += num%10
rev_num =rev_num * 10

num = num//10
rev_num += num%10
rev_num =rev_num * 10

num = num//10
rev_num += num

# while(num):
#     rev_num = num%10
#     num = num/10

print("Enter revers number is - ", str(rev_num))