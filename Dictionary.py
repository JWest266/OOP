from dataclasses import replace
myStudents = {}
while 1:
    print("1. Add a record to the directory")
    print("2. Delete a record to the directory")
    print("3. Replace a record to the Directory")
    print("4. Print the Dictionary")
    print("5. Quit")

    option = input()

    if option == "1":
        sid = input("Student ID", )
        nname = input("Enter Name", )
        mmajor = input("Enter Major", )
        yyear = input("Enter year", )
        ttc = input("Total credit hours", )
        ggpa = input("Enter your gpa", )

        myStudents.update({sid: {
            "name": nname,
            "Major": mmajor,
            "year": yyear,
            "Tcredits": ttc,
            "GPA": ggpa
        }})
        for student_record in myStudents.items():
            print(student_record)
            print("-------------------------------")

    elif option == "2":
        sid = input("Enter ID you choose to delete")
        if sid in myStudents:
            del myStudents[sid]
            print("deleted student {sid}")
        else:
            print("User not found")

    elif option == "3":
        sid = ("Enter record you would like to replace")
        if sid in myStudents:
            nname = input("Enter new Name: ")
            mmajor = input("Enter new Major: ")
            yyear = input("Enter new Year: ")
            ttc = input("Enter new Total credit hours: ")
            ggpa = input("Enter new GPA: ")

            myStudents[sid] = {
                "name": nname,
                "Major": mmajor,
                "year": yyear,
                "Tcredits": ttc,
                "GPA": ggpa
            }
            print(f"Replaced student {sid}.")
        else:
            print("Student ID not found.")

    elif option == "4":
        if myStudents:
            for sid, info in myStudents.items():
                print(f"ID: {sid}")
                for key, value in info.items():
                    print(f"  {key}: {value}")
                print("-------------------------")
        else:
            print("No records found.")


    elif option == "5":
        print("exiting program")
        break

    else:
        print("invalid option, try again")


