authorised_users = {
    'admin': 'superadmin',
    'viktor': 'password123'
}

user = 'admin'

if user not in authorised_users:
    print('Not found')
else:
    print(authorised_users[user])
