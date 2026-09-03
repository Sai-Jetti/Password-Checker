print('Hello, Welcome to the Password Checker!')
password = input ('Please enter your password: ')

count = 0
if len(password) <= 8:
    count += 1
have_upper = False
have_lower = False
have_digit = False
have_special = False
special = '!@#$%^&*()_-+='

for char in password:
    if char.isupper():
        have_upper = True
    if char.islower():
        have_lower = True
    if char.isdigit():
        have_digit = True
    if char in special:
        have_special = True

if have_upper == True:
    count += 1
if have_lower == True:
    count +=1
if have_digit == True:
    count += 1
if have_special == True:
    count += 1

if count == 5:
    print('Your password is strong!')
elif count == 4:
    print('Your password is decent but could be stronger.')
else:
    print('Your password is weak. Please consider making it stronger.')

if have_upper == False:
    print('Your password does not contain any uppercase letters. Please consider adding an uppercase letter to improve its strength.')
if have_lower == False:
    print('Your password does not contain any lowercase letters. Please consider adding a lowercase letter to improve its strength.')
if have_digit == False:
    print('Your password does not contain any numbers. Please consider adding a number to improve its strength.')
if have_special == False:
    print('Your password does not contain any special characters. Please consider adding a special character to improve its strength.')

print('test')
combination = 0
if have_upper == True:
    combination += 26
if have_lower == True:
    combination += 26
if have_digit == True:
    combination += 10
if have_special == True:
    combination += len(special)
attempts = combination ** len(password)

seconds = attempts / 1000000000
years = seconds / 60 / 60 / 24 / 365

print(f'The number of possible combinations for your password is: {attempts:,} and the estimated time to crack it is: {years:,.2f} years.')
    