# 13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit -> l0
# For next 100 units Rs. 0.75/unit -> l1
# For next 100 units Rs. 1.20/unit -> l2
# For unit above 250 Rs. 1.50/unit -> l3
# An additional surcharge of 20% is added to the bill

unit = float(input('Enter the electricity Unit: '))
bill = 0
act_unit = unit
l3_bill=0
l2_bill=0
l1_bill=0
l0_bill = 0

#First way - 1
if unit > 250:
    l3 = unit - 250
    l3_bill = l3 * 1.50
    unit -= l3

if ((unit <= 250) and(unit>150)):
    l2 = unit - 100
    l2_bill = l2 * 1.2
    unit -= l2

if ((unit <= 150) and (unit>50)):
    l1 = unit - 50
    l1_bill = l1 * 0.75
    unit -= l1

if unit <= 50:
    l0_bill = unit * 0.50
    unit -= unit

bill = l3_bill + l2_bill + l1_bill + l0_bill

bill = bill + (bill * 20/100)

print(f'electricity bill of {act_unit} unit is - {bill}.')

#
# #2nd way
# if unit > 250:
#     bill = (unit-250)*1.5
#     unit -= 250
#     if ((unit <= 250) and (unit > 150)):
#         bill = (unit-150)*1.2
#         unit -= 150
#     if ((unit <= 150) and (unit>50)):
#         bill = (unit - 50)*0.75
#         unit -= 100
#     if unit< 50:
#          bill = unit*0.5   
    