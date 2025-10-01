title = input('Enter the title: ')

shopping_list = ''
total_cost = 0
count = 0

while True:

    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print()

    choice = input('Enter your choice: ')

    if choice == '1':
        item = input('Enter an item: ')
        price = int(input('Enter item price: '))
        shopping_list += item + '\n'
        total_cost += price
        count += 1

    elif choice == '2':
        print('Currently added items:')
        print(shopping_list)

    elif choice == '3':
        average = total_cost / count
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        print(shopping_list)
        print(f'Average price: {average:.2f} SEK')
        break
    
    else:
        print('Error: Invalid choice, please try again.')
