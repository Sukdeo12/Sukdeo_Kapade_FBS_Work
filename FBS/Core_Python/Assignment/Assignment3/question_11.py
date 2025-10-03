'''11. Accept age of five people and also per person ticket amount and then calculate total
amount to ticket to travel for all of them based on following condition :
a. Children below 12 = 30% discount
b. Senior citizen (above 59) = 50% discount
c. Others need to pay full.
'''

pr1 = input("Enter the name 1st person:")
age1 = int(input('Enter the age for 1st person:'))
amaunt1 = float(input('Enter the amount of ticke:'))


if age1 and amaunt1:
    if age1 < 12 :
        act_amout_1 = (amaunt1 - (amaunt1 * (30/100)))   
    elif (age1 > 59):
        act_amout_1 = (amaunt1 - (amaunt1 * (50/100)))
    else:
        act_amout_1 = amaunt1  


pr2 = input("Enter the name 2nd person:")
age2 = int(input('Enter the age for 2nd person:'))
amaunt2 = float(input('Enter the amount of ticke:'))


if age2 and amaunt2:
    if age2 < 12 :
        act_amout_2 = (amaunt2 - (amaunt2 * (30/100)))   
    elif (age1 > 59):
        act_amout_2 = (amaunt2 - (amaunt2 * (50/100)))
    else:
        act_amout_2 = amaunt12  

pr3 = input("Enter the name 3rd person:")
age3 = int(input('Enter the age for 3rd person:'))
amaunt3 = float(input('Enter the amount of ticke:'))


if age3 and amaunt3:
    if age3 < 12 :
        act_amout_3 = (amaunt3 - (amaunt3 * (30/100)))   
    elif (age3 > 59):
        act_amout_3 = (amaunt3 - (amaunt3 * (50/100)))
    else:
        act_amout_3 = amaunt3  

pr4 = input("Enter the name 4rth person:")
age4 = int(input('Enter the age for 4rth person:'))
amaunt4 = float(input('Enter the amount of ticke:'))


if age4 and amaunt4:
    if age4 < 12 :
        act_amout_4 = (amaunt4 - (amaunt4 * (30/100)))   
    elif (age4 > 59):
        act_amout_4 = (amaunt4 - (amaunt4 * (50/100)))
    else:
        act_amout_4 = amaunt4  



pr5 = input("Enter the name 5th person:")
age5 = int(input('Enter the age for 5th person:'))
amaunt5 = float(input('Enter the amount of ticke:'))


if age5 and amaunt5:
    if age5 < 12 :
        act_amout_5 = (amaunt5 - (amaunt5 * (30/100)))   
    elif (age5 > 59):
        act_amout_5 = (amaunt5 - (amaunt5 * (50/100)))
    else:
        act_amout_5 = amaunt5  

print(f'name is {pr1}, age is : {age1} and amount is: {act_amout_1}')
print(f'name is {pr2}, age is : {age2} and amount is: {act_amout_2}')
print(f'name is {pr3}, age is : {age3} and amount is: {act_amout_3}')
print(f'name is {pr4}, age is : {age4} and amount is: {act_amout_4}')
print(f'name is {pr5}, age is : {age5} and amount is: {act_amout_5}')

total_amount = (act_amout_1 + act_amout_2 + act_amout_3 + act_amout_4 + act_amout_5)
print(f'The total amount is : {total_amount}')