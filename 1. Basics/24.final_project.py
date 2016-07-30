from statistics import mean
#import getpass as g
import re


authorised_users = dict(admin='superadmin', viktor='password123')

all_grades = dict(Bob=[65,77,33], Sam=[44,66,77], Nic=[76,54,95])

def authenticate():
    print('Welcome to the grading system. Please identify yourself')
    user = str(input('Username: '))
    #password = str(g.getpass()) - doesnt work here
    password = str(input('Password: '))
    if user not in authorised_users:
        print('Sorry, this username is not recognised')
    else:
        if password != authorised_users[user]:
            # Check the password isn't empty - indefinitely
            while len(password) == 0:
                print('The password field cannot be empty. Please try again')
                password = str(input('Password: '))
            else:
                for i in range(0, 3):
                    print('The password you entered is incorrect')
                    print('Please try again or press Ctrl + C to exit')
                    password = str(input('Password: '))
                # Quit after 3 attempts
                print('No more attempts left. Goodbye!')
        else:
            print('You have successfully logged in!')

def main_menu():
    print('''
    You have the followig options:

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Get Grade Average
    [4] - Exit

    ''')
    user_choice = input(' What would you like to do today? ')
    # Check that there are only numbers, and the valid number has been passed
    while re.match("[a-zA-Z]", user_choice) or re.match("[\W+]", user_choice) or int(user_choice) not in range(1, 5):
            print('Invalid Input! Please enter a number between 1 and 4 to indicate the option you want')
            user_choice = input(' What would you like to do today? ')
    else:
        choice = int(user_choice)
        if choice == 1:
            student = str(input('Please enter the student\'s name: '))
            get_grades = input('Please enter their grades, separated by commas: ')
            grades = [int(grade) for grade in get_grades.split(',')]
            all_grades[student] = grades
            print('The current list of studesnts is:')
            for student in all_grades:
                print(student, ':', all_grades[student])

main_menu()