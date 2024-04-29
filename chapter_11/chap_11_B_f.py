users = {
    'Sanjay': 'ceftum1250', 'Rahul': 'Crocin100',
    'Sanket': 'Metrogyl50', 'Shyam': 'Miopass10',
    'Satish': 'mvpxx_9000', 'Srishti': 'Relaxo!',
    'Smriti': 'newyear200', 'Sakhi': 'Bday1711',
    'Raakhi': 'jallosh200', 'Rahika': 'Ultu1900'
}

user_name = input('Enter username: ')
password_user = input('Enter passowrd: ')

if user_name in users and users[user_name] == password_user:
    print("Correct credentials!")
else:
    print("Chor ho tum mukesh!!")


# second method
# user_name = input('Enter username: ')
# password_user = input('Enter passowrd: ')

# if users.get(user_name) == password_user:
#     print("Correct credentials!")
# else:
#     print("Chor ho tum mukesh!!")
