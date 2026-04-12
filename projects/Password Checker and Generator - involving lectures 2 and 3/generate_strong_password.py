# Filename: generate_strong_password.py
# Function: Generate a random password with the length specified by the user
# Author: Rodrigo de Souza Galvão
# Last Modification: April 12th 2026
# Project Including Concepts from Lectures 2 and three from MIT python course

import console_treat as console
import string
import random

def choose_character(pattern: str) -> str:
    return random.choice(pattern)
    

def generate_strong_password():
    # defines the password and add one of every required character
    password = ''
    password += choose_character(string.ascii_lowercase)
    password += choose_character(string.digits)
    password += choose_character(string.ascii_uppercase)
    password += choose_character(string.punctuation)

    # pattern with all available characters
    all_chars = string.punctuation + string.ascii_letters + string.digits
    
    console.clear()
    print('How long should the password be? (Use at least 8 characters)')

    # evaluate and check user value
    while True:
        try:
            length = int(input())

            if length < 8:
                print('Password length must be at least 8 characters')
            else:
                break
        except ValueError:
            print('Enter only an integer number: ')
    
    # insert random chars into the password
    for _ in range(length - 4):
        password += choose_character(all_chars)

    # shuffle the list
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # reveals the password for the user
    print(f"""
    Generated password: {password}
    Length: {length}
    """)

    console.pause()

