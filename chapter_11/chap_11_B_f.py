users = {
    'Sanjay': 'ceftum1250', 'Rahul': 'Crocin100',
    'Sanket': 'Metrogyl50', 'Shyam': 'Miopass10',
    'Satish': 'mvpxx_9000', 'Srishti': 'Relaxo!',
    'Smriti': 'newyear200', 'Sakhi': 'Bday1711',
    'Raakhi': 'jallosh200', 'Rahika': 'Ultu1900'
}

user_name = input('Enter username: ')
password_user = input('Enter passowrd: ')

for user, password in users.items():
    if user == user_name and password == password_user:
        print("Correct credentials!")


print("Chor ho tum mukesh!! ")
