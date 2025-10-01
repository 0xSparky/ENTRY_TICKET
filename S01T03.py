title = input('Enter the title:')
print('')
shopping_list = '' 

while True:
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')

    choice = int(input('Enter your choice: '))
    if choice == 1:
        item = input('Enter an item: ')
        quantity = int(input('Enter quantity:')) #changed from float to int
        formatted = f'{item:<10}x{quantity:>9}'
        
        shopping_list += formatted + '\n'
        
    elif choice == 2:
        print('Currently added items:')
        print(shopping_list)
    
    elif choice == 3:
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        #if shopping_list=='':
        #    print('no items ')
        #else:
        print(shopping_list)
        break
    
    else:
        print('Error: Invalid choice, please try again.')



