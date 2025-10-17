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
    number = int(input('Number: '))
    time = int(input('Time: '))
    print()
    initial_value = tuple([number, time])
    test_subjects.append(initial_value)

# write data to file        == w)
def write_data(test_subjects, filename):
    with open(filename, 'w') as f:
        for number, time in test_subjects:
            f.write(f"{number}\n{time} \n")
        

# read data                 == r)
def read_data(filename):
    file_item = []
    with open(filename, 'r') as file:
        file = [line.strip() for line in file.readlines()]

        for i in range (0, len(file), 2):
            number = file[i]
            time = file[i + 1]

            file_item.append((number, time))
    print(file_item)

# print test subjects       == s)
def print_test_subjects(test_subjects):
    print('-' * 4, 'Registered test subjects', '-' * 4, sep=' ')
    if test_subjects != '':
        for i,j in test_subjects:
            print(f"Number : {i}")
            print(f"Time   : {j}")
            print()




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
