from statistics import mean
#import getpass as g
import re
import sys


authorised_users = dict(admin='superadmin', viktor='password123')

all_grades = dict(Bob=[65, 77, 33], Sam=[44, 66, 77], Nic=[76, 54, 95])


def print_students():
    print('The current list of students is:')
    for student in all_grades:
        print(student, ':', all_grades[student])


def check_name(message):
    student = input(message)
    while student not in all_grades:
        print('Name not recognised!')
        student = input(message)
    else:
        return student

def show_menu():
    print('''
        You have the followig options:\n
        [1] - Enter Grades
        [2] - Remove Student
        [3] - Get Grade Average
        [4] - Show students' records
        [5] - Show menu
        [6] - Exit\n
        ''')

def authenticate():
    print('Welcome to the grading system. Please identify yourself')
    user = str(input('Username: '))
    #password = str(g.getpass()) - doesnt work here
    password = str(input('Password: '))
    if user not in authorised_users:
        print('Sorry, this username is not recognised')
        sys.exit(0)
    else:
        while len(password) == 0:
            # Check the password isn't empty - indefinitely
            print('The password field cannot be empty. Please try again')
            password = str(input('Password: '))
        else:
            login_attempts = 0
            while password != authorised_users[user]:
                login_attempts += 1
                if login_attempts == 3:
                    # Quit after 3 attempts
                    print('No more attempts left. Terminating!!!!')
                    sys.exit(2)
                else:
                    print('The password you entered is incorrect')
                    print('Please try again or press Ctrl + C to exit')
                    password = str(input('Password: '))
            else:
                print('You have successfully logged in!')


def main_menu():
    authenticate()
    show_menu()
    while True:
        user_choice = input('What would you like to do today? (Enter 5 for help): ')
        # Check that there are only numbers, and the valid number has been passed
        while re.match("[a-zA-Z]", user_choice) or re.match("[\W+]", user_choice) or int(user_choice) not in range(1, 7):
                print('Invalid Input! Please enter a number between 1 and 6 to indicate the option you want')
                user_choice = input('What would you like to do today? (Enter 5 for help): ')
        else:
            choice = int(user_choice)

            if choice == 1:
                student = str(input('Please enter the student\'s name: '))
                get_grades = input('Please enter their grades, separated by commas: ')
                grades = [int(grade) for grade in get_grades.split(',')]
                all_grades[student] = grades
                print_students()

            elif choice == 2:
                student = check_name('Which student would you like to remove?: ')
                print('The system currently has the following information about', student, ':')
                print(student, all_grades[student])
                confirm = str(input('Are you sure you want to delete this person?: ')).lower()
                while confirm != 'yes' and confirm != 'no':
                    print('Please enter Yes or No')
                    confirm = str(input('Are you sure you want to delete this person?: ')).lower()
                else:
                    if confirm == 'yes':
                        print('Deleting all entries for', student)
                        del all_grades[student]
                        print_students()
                    elif confirm == 'no':
                        print('Aborting the operation...')

            elif choice == 3:
                student = check_name('Whose grade average would you like to see?: ')
                print(student, ':', all_grades[student])
                print('Their average is: %.2f' % mean(all_grades[student]))

            elif choice == 4:
                print_students()

            elif choice == 5:
               show_menu()

            elif choice == 6:
                print('Goodbye!')
                sys.exit(0)

main_menu()