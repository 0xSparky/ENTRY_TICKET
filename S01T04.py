title = input("Enter the title: ")
print("")
shopping_list = ""
while True:
    print("1. Add an item")
    print("2. Print currently added items")
    print("3. Finished")
    # adding a new menu
    print("R. Reset shopping list")

    choice = input(
        "Enter your choice :"
    ).upper()  # changed to make all input upper case
    if choice == "1":
        item = input("Enter an item:")
        shopping_list += item + "\n"

    elif choice == "2":
        print("Currently added items:")
        # if shopping_list.strip()=='':
        #    print('(no items yet)')
        # else:
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
            print("Shopping list has been reset.\n")
        else:
            print("Reset cancelled.\n")
    else:
        print("Error: Invalid choice, please try again.\n")
 