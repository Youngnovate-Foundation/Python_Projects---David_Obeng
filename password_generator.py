"""
    Password Generator App
    David Obeng Atiemo-Keseku

"""

import string
import secrets

lower = string.ascii_lowercase
upper = string.ascii_uppercase
special_char = string.punctuation

print('\n')
print('========================================')
print("Welcome to the Password Generator App!")
print('======================================== \n')

while True:
    length = int(input('Input length of Passowrd (Password must have at least 8 Characters): '))
    print('\n')
    if length >= 8:
        break
    else:
        print('Input a number greater than 8. \n')

while True:
    choice = input('Include special characters in password (yes/no): ').lower()
    print('\n')
    if choice == 'yes':
        char = lower + upper + special_char
        break
    elif choice == 'no':
        char = lower + upper
        break
    else:
        print("Input must be 'Yes' or 'No' for special characters inclusion. \n")

password = ''.join(secrets.choice(char) for i in range(length))
print(f"Generated Password {password}")