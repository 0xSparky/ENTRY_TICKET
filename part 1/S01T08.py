title = input('Enter the title: ')

shopping_list = ''
highest_price = 0

while True:

    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
    print()

    choice = input('Enter your choice: ')

    if choice == '1':
        item = input('Enter an item: ')
        price = float(input('Enter item price: '))
        shopping_list += item + '\n'

        if price > highest_price:
            highest_price = price

    elif choice == '2':
        print('Currently added items:')
        print(shopping_list)

    elif choice == '3':
        print('-'*20)
        print(title.center(20))
        print('-'*20)
        print(shopping_list)
        print(f'Most expensive item: {highest_price:.3f} SEK')
        break
    
    else:
        print('Error: Invalid choice, please try again.')
