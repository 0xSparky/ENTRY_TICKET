#!/bin/python3

test_subjects = [] # empty list

# menu function
def print_menu():
    print('-' * 9, ' Menu ', '-' * 10, sep='')
    print('a) Add a new test subject')
    print('s) Show all information')
    print('r) Read from file')
    print('w) Write to file')
    print('q) Quit')
    print('-' * 25)

# adding new test subject  == a)
def new_test_subject():
    pass

# write data to file        == w)
def write_data(test_subjects, filename):
    pass

# read data                 == r)
def read_data(filename):
    pass

# print test subjects       == s)
def print_test_subjects(test_subjects):
    pass




def main():
    while True:
        print_menu()
        
        choice = input('Your choice: ')

        if choice == 'a':
            new_test_subject()
        elif choice == 's':
            print_test_subjects(test_subjects)
        elif choice == 'r':
            filename = input('Filename: ')
            read_data(filename)
        elif choice == 'w':
            filename = input('Filename: ')
            write_data(test_subjects, filename)
        elif choice == 'q':
            break
        else:
            continue


if __name__ == '__main__':
    main()