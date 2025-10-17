title = input('Enter the title: ')
date = input('Enter the date: ')

if title == '':
    title = '(No title)'

if date == '':
    date = '(No date)'

title_date = title + ' ' + date

shopping_list = ''

while True:
    
    print()
    print('1. Add an item')
    print('2. Print currently added items')
    print('3. Finished')
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
        print(title_date.center(20))
        print('-'*20)
        print(shopping_list)
        break
    
    else:
        print('Error: Invalid choice, please try again.')
