# Password Strength Checker + Generator
# A program where the user can:
# Enter a password → your program analyzes how strong it is
# Optionally generate a stronger password

# Filename: main.py
# Function: Allows user to interact with the system
# Author: Rodrigo de Souza Galvão
# Last Modification: April 12th 2026
# Project Including Concepts from Lectures 2 and three from MIT python course

import console_treat as console
import check_password as check
import generate_strong_password as generate


while True:
    console.clear()
    print('1 - Check password strength\n2 - Generate password\n3 - Exit\n')

    while True:
        try:
            menu = int(input('Choose what you want to do: '))
            break
        except ValueError:
            print(f'Invalid input. Please enter a valid number: ')

    match menu:
        case 1:
            check.check_password()
        case 2:
            generate.generate_strong_password()
        case 3:
            print('Thanks for using the password check system')
            break
        case _:
            print('Invalid option. Try again')
            console.pause()
            

