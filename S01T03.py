title = input('Enter the title:')

shopping_list = '' 

while True:
    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print()

    choice = int(input('Enter your choice: '))
    
    if choice == 1:
        item = input('Enter an item: ')
        quantity = int(input('Enter quantity:')) 
        formatted = f'{item:<10}x{quantity:>9}'
        
        shopping_list += formatted + '\n'
        
    elif choice == 2:
        print('Currently added items:')
        print(shopping_list)
    
    elif choice == 3:
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        print(shopping_list)
        break
    
    else:
        print('Error: Invalid choice, please try again.')





