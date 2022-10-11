#password checker excercise
username = input('enter a username')
password = input('enter a password')

password_length = len(password)
hidden_password = '*' *password_length

print(f'{username}, Your password, {hidden_password}, is {len(password)}')