from statistics import mean
#import getpass as g


authorised_users = dict(admin='superadmin', viktor='password123')

grades = dict(Bob=[65,77,33], Sam=[44,66,77], Nic=[76,54,95])

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
                for i in range(0,3):
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
    try:
        user_choice = int(input(' What would you like to do today? '))
    except Exception as e:
        print('Invalid Input!')
        while user_choice not in range(1, 5):
            print('Please select one of the options from the menu')
            user_choice = int(input(' What would you like to do today? '))
        else:
            print()


main_menu()