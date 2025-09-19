# Notes = 5000
#how many notes required for 500, 200, 100, 500 and 10 rps to pay
Note = int(input("Enter the Notes : "))
print("Note is - ", Note)
R_Note = Note
flag = False
FH_Note = 0
TwoH_Note = 0
OneH_Note = 0
Fifty_Note = 0
Ten_Note = 0
remaining = 0

if Note >= 500:
    FH_Note = Note//500
    Note = Note%500
    flag = True
if 500 > Note >= 200:
    TwoH_Note = Note//200
    Note = Note%200
    flag = True
if 200 > Note >= 100:
    OneH_Note = Note//100
    Note = Note%100
    flag = True
if 100 > Note >= 50:
    Fifty_Note = Note//50
    Note = Note%50
    flag = True
if 50>Note >= 10:
    Ten_Note = Note//10
    Note = Note%10
    flag = True   
if 10>Note>0:
    remaining = Note
    flag = True

if flag:
    if FH_Note:
        print("500 Hundres Notes : " + str(FH_Note))
    if TwoH_Note: 
        print(" and 200 Hundred Notes : " + str(TwoH_Note))
    if OneH_Note:
        print(" and 100 Hundred Notes : " + str(OneH_Note))
    if Fifty_Note:
        print(" and 50 Notes : " + str(Fifty_Note))
    if Ten_Note:
        print(" and 10 Notes : " + str(Ten_Note))
    if remaining:
        print("less than 10 rs Note : ", Note)     
        
    Min_Notes = FH_Note + TwoH_Note + OneH_Note + Fifty_Note + Ten_Note
    print(f'Min Number of notes are : {Min_Notes}')
    
else:
    print("Note value Not Valied", Note)  