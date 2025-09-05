while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    option = input("Enter your choice")

    if option == "1":
        n1 = int(input("Enter number ", ))
        n2 = int(input("Enter number ", ))
        print(n2 + n1)

    elif option == "2":
        n1 = int(input("Enter number ", ))
        n2 = int(input("Enter number ", ))
        print(n1 - n2)

    elif option == "3":
        n1 = int(input("Enter number ", ))
        n2 = int(input("Enter number ", ))
        print(n1 * n2)

    elif option == "4":
        n1 = int(input("Enter number ", ))
        n2 = int(input("Enter number ", ))
        print(n1/n2)

    elif option == "5":
        choice = input("Type yes or no")

        if choice == "yes":
            print("Thank you for using the application")
            break

        elif choice == "no":
            print("ok")
