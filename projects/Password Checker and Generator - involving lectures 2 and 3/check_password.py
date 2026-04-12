# Filename: check_password.py
# Function: Check and evaluate a password
# Author: Rodrigo de Souza Galvão
# Last Modification: April 12th 2026
# Project Including Concepts from Lectures 2 and three from MIT python course

import console_treat as console
import string

def check_for_value(password: str, pattern: str) -> bool:
    for char in password:
        if char in pattern:
            return True
        
    return False

def check_password():
    console.clear()
    password = input('Enter your password to check: ')

    # variable to check in the password
    length = len(password)
    has_uppercase = check_for_value(password, string.ascii_uppercase)
    has_lowercase = check_for_value(password, string.ascii_lowercase)
    has_number = check_for_value(password, string.digits)
    has_special_char = check_for_value(password, string.punctuation)

    # password evaluation
    score = 0
    password_level = ''

    # suggestions for password
    suggestions = []

    if length >= 8:
        score += 1
    else:
        suggestions.append('- Make it longer')
    if has_uppercase:
        score += 1
    else:
        suggestions.append('- Add an uppercase character')
    if has_lowercase:
        score += 1
    else: 
        suggestions.append('- Add a lowercase character')
    if has_number:
        score += 1
    else:
        suggestions.append('- Add a number')
    if has_special_char:
        score += 1
    else: 
        suggestions.append('- Add a special character')
    
    if score <= 2:
        password_level = 'Weak password!'
    elif score == 3 or score == 4:
        password_level = 'Medium password!!'
    else:
        password_level = 'Strong password!!!!!'

    print(f"""
    Length: {length}
    Uppercase: {has_uppercase}
    Lowercase: {has_lowercase}
    Number: {has_number}
    Special char: {has_special_char}

    Password Strength: {password_level}
    Score: {score}/5
    """)

    if suggestions:
        print('\nSuggestions:')
        for s in suggestions:
            print(s)

    console.pause()