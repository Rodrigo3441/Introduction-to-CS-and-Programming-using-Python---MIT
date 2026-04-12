# Password Strength Checker + Generator

## Overview

This project is a simple Python application that allows users to:

* Check the strength of a password
* Generate a strong random password

It was developed as practice based on **Lectures 2 and 3** (Strings, Input/Output, Branching, and Iteration) from the MIT Python course.

---

## Concepts Practiced

This project demonstrates the use of:

* **Strings** → analyzing and building passwords
* **Input/Output** → user interaction via terminal
* **Branching (`if`, `match-case`)** → decision-making logic
* **Iteration (`for`, `while`)** → loops for validation and generation
* **Functions** → modular and reusable code
* **Modules** → separation of concerns across files
* **Error Handling (`try/except`)** → safe input validation

---

## Project Structure

```
project-folder/
│
├── main.py
├── check_password.py
├── generate_strong_password.py
└── console_treat.py (custom utility for clear/pause)
```

---

## Features

### Password Strength Checker

* Analyzes:

  * Length
  * Uppercase letters
  * Lowercase letters
  * Numbers
  * Special characters
* Provides:

  * Strength score (0–5)
  * Classification (Weak / Medium / Strong)
  * Suggestions for improvement

---

### Password Generator

* User defines desired length (minimum: 8)
* Automatically ensures:

  * At least one uppercase letter
  * At least one lowercase letter
  * At least one number
  * At least one special character
* Randomizes character positions for better security

---

### Interactive Menu

* Loop-based system that allows:

  * Checking passwords
  * Generating passwords
  * Exiting the program

---

## How to Run

1. Make sure you have Python installed (Python 3.10+ recommended for `match-case`)
2. Run the main file:

```bash
python main.py
```

---

## Example Usage

```
1 - Check password strength
2 - Generate password
3 - Exit

Choose what you want to do:
```

---

## Possible Improvements

* Save generated passwords to a file
* Add user preferences (include/exclude symbols)
* Detect common weak passwords
* Add a graphical interface (GUI or web version)
* Turn into a login/authentication system

---

## Author

**Rodrigo de Souza Galvão**

---

## Last Update

April 12, 2026

---

## License

This project is for educational purposes.
