student_name = input("Enter Student's Name: ")
course1 = int(input("Enter the grade for course1: ") )
course2 = int(input("Enter the grade for course2: ") )
course3 = int(input("Enter the grade for course3: ") )
course4 = int(input("Enter the grade for course4: ") )
course5 = int(input("Enter the grade for course5: ") )

total = course1+course2+course3+course4+course5
Average = total/5
total_percentage = ((total/500)*100)

if total_percentage < 100 and total_percentage > 90:
    print("Grade A")
elif total_percentage > 80 and total_percentage < 89:
    print("Grade B")
elif total_percentage > 70 and total_percentage <79:
    print("Grade C")
elif total_percentage > 60 and total_percentage <69:
    print("Grade D")
elif total_percentage > 0 and total_percentage < 59:
    print("Grade F")
print("Your total is:", total)
print("Your average is:", Average)

