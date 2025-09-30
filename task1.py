title = input('Enter the title: ')
stored_data = ''
count = 0
while True:

    print('\n1. Add an item')
    print('2. Print currently added items')
    print('3. Finished\n')

    choice = input('Enter your choice: ')


    if choice == '1':
        data = input('Enter an item: ')
        stored_data += (data + '\n')
        continue
    
    elif choice == '2':
        if stored_data == '':
            print('The shopping list is empty.')
        else:    
            print('Currently added items:')
            print(stored_data)

    elif choice == '3':
        print('-' * 20)
        print(f'{title.center(20)}')
        print('-' * 20)
        print(stored_data)
        print()
        break
        

    else:
        print('Error: Invalid choice, please try again.')
        continue