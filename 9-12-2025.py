MyListy = []

while True:
    print("1. Add an element to the List")
    print("2. Remove an element from the List")
    print("3. Replace the last element")
    print("4. Reverse the elements in the list")
    print("5. Sort Elements in the list")
    print("6. Display the List")
    print("7. Quit")

    option = input("Enter your choice:", )
    if option == "1":
        n = int(input("Add a number to the list", ))
        MyListy.append(n)

    elif option == "2":
        b = int(input("Remove a number from the list", ))
        MyListy.remove(b)

    elif option == "3":
        x = int(input("What is the index of the element to be replaced, "))
        new_element = int(input("Enter new value, "))
        MyListy[x] = new_element

    elif option == "4":
        MyListy.reverse()
        print("Done")

    elif option == "5":
        MyListy.sort()
        print("The list has been sorted")

    elif option == "6":
        print(MyListy)

    elif option == "5":
        break