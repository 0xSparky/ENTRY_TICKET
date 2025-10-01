title = input('Enter the title: ')

shopping_list = ''
price = 0

while True:
    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print('C. Calculate prices')
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
        for i in range (0, 3):
            price += int(input('Enter price: '))
        print(f'Total price: {price:>5} SEK')
        
    else:
        print('Error: Invalid choice, please try again.')

