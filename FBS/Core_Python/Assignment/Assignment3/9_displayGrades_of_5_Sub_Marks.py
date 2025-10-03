#Question - Input 5 subject marks from user and display grade(eg.First class,Second class ..)
sub1 = float(input("Enter the sub 1 marks : "))
sub2 = float(input("Enter the sub 2 marks : "))
sub3 = float(input("Enter the sub 3 marks : "))
sub4 = float(input("Enter the sub 4 marks : "))
sub5 = float(input("Enter the sub 5 marks : "))

total_m_perc = (sub1+sub2+sub3+sub4+sub5)/5
grade = None
#Define grades 
#A+ -> 95 - 100%
#A  -> 94 - 85%
#B -> 84 - 70 %
#C -> 69 - 55%
#D -> 54 - 35%
#F -> 34% or less

if total_m_perc >= 95:
    grade = 'A+'
elif ((95 > total_m_perc) and (total_m_perc >= 85)):
    grade = 'A'
elif ((85 > total_m_perc) and (total_m_perc >= 70)):
    grade = 'B'
elif ((70 > total_m_perc) and (total_m_perc >= 55)):
    grade = 'C'
elif ((54 > total_m_perc) and (total_m_perc >= 35)):
    grade = 'D'
else:
    grade = 'F'    

print(f'Total mark in perc is : {total_m_perc}, and your grade is : {grade}.')