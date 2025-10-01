title = input('Enter the title: ')

shopping_list = ''

while True:

    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print('C. Change title')
    print()

    choice = input('Enter your choice: ')

    if choice == '1':
        item = input('Enter an item: ')
        shopping_list += item + '\n'

    elif choice == '2':
        print('Currently added items:')
        print(shopping_list)

    elif choice == '3':
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        print(shopping_list)
        break
    
    elif choice == 'C':
        new_title = input('New title: ')

        if new_title == title:
            print('INFO: The new title is the same as the old one.')
        elif new_title == '':
            print('ERROR: Title can not be empty.')
        else:
            title = new_title
            
    else:
        print('Error: Invalid choice, please try again.')
