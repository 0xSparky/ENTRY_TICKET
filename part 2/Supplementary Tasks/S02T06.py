#!/bin/python3

# menu function
def print_menu():
    print()
    print('-' * 9, ' Menu ', '-' * 10, sep='')
    print('a) Add a new test subject')
    print('s) Show all information')
    print('r) Read from file')
    print('w) Write to file')
    print('q) Quit')
    print('-' * 25)
    print()

# adding new test subject  == a)
def new_test_subject():
    number = (input('Number :   '))
    time = read_int('Time   : ')
    print()
    return (number, time)

# write data to file        == w)
def write_data(test_subjects, filename):
    with open(filename, 'w+') as f:
        for number, time in test_subjects:
            f.write(f'{number}\n{time}\n')
        

# read data                 == r)
def read_data(filename):
    data = [] # empty list to contain tuple
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file.readlines()] # making a temporary list to store single data

        for i in range (0, len(lines), 2):
            number = lines[i]
            time = int(lines[i + 1])
            data.append((number,time))
    return data

# print test subjects       == s)
def print_test_subjects(test_subjects):
    print('-' * 4, 'Registered test subjects', '-' * 4, sep=' ')
    if test_subjects != []:
        for i,j in test_subjects:
            print(f"Number :{i:>5}")
            print(f"Time   :{j:>5}")
            print()

def read_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print('ERROR: Please enter an integer number.')




def main():
    test_subjects = [] # empty list
    while True:
        print_menu()
        
        choice = input('Your choice: ')

        if choice == 'a':
            test_subjects.append(new_test_subject())

        elif choice == 's':
            print_test_subjects(test_subjects)

        elif choice == 'r':
            filename = input('Filename: ')
            test_subjects = read_data(filename)
            print()
            print('*' * 3, 'Data read from file', '*' * 3, sep=' ')

        elif choice == 'w':
            filename = input('Filename: ')
            write_data(test_subjects, filename)
            
        elif choice == 'q':
            break
        else:
            continue


if __name__ == '__main__':
    main()
