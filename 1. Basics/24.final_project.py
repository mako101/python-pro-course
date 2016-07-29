authorised_users = {
    'admin': 'superadmin',
    'viktor': 'password123'
}

def authenticate():
    print('Welcome to the grading system. Please identify yourself')
    username = input('Username: ')
    password = input('Password: ')