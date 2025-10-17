title = input('Enter the title: ')
stored_data = ''
total_cost = 0
while True:

    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print()

    choice = input('Enter your choice: ')

    if choice == '1':
        data = input('Enter an item: ')
        price = int(input('Price: '))
        count = int(input('How many:'))
        stored_data += (data + '\n')
        total_cost += (price * count) 
    
    elif choice == '2':
        print('Currently added items:')
        print(stored_data)

    elif choice == '3':
        print('-' * 20)
        print(f'{title.center(20)}')
        print('-' * 20)
        print(stored_data)
        print(f'Total cost: {total_cost:.2f} SEK')
        print()
        break
        
    else:
        print('Error: Invalid choice, please try again.')
