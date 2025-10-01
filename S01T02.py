title = input('Enter the title: ')

shopping_list = '' 
counter_item = 0

while True :
    
    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print('S. Show number of addded items')
    print()

    choice=input('Enter your choice: ')
    
    if choice == '1':
        item = input('Enter an item: ')
        shopping_list += item + '\n'
        counter_item += 1

    elif choice == '2':
        print('Currently added items:')
        print(shopping_list)

    elif choice == '3':
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        print(shopping_list)
        break
    
    elif choice == 'S':
        print(f'Currently the list contains {counter_item} items')    
        
    else:
        print('Error: Invalid choice, please try again.')







