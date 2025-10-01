title = input("Enter the title: ")
shopping_list = ""

while True:
    print()
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    print("R. Reset shopping list")
    print()

    choice = input("Enter your choice :")
    
    if choice == "1":
        item = input("Enter an item:")
        shopping_list += item + "\n"

    elif choice == "2":
        print("Currently added items:")
        print(shopping_list)

    elif choice == "3":
        print("_" * 20)
        print(title.center(20))
        print("_" * 20)
        print(shopping_list)
        break

    elif choice == "R":
        confirm = input("Are you sure (y/n)?")
        if confirm == "y":
            shopping_list = ""
            print("Shopping list has been reset.)
        else:
            print("Reset cancelled.")
    else:
        print("Error: Invalid choice, please try again.")

 
