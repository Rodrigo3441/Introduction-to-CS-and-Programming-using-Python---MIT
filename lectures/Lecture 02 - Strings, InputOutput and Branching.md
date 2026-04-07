
## Strings

- Think of a str as a sequence of case sensitive characters
	- Letters, special characters, spaces, digits
- Enclose in quotation marks or single quotes
	- Just be consistent about the quotes
	- a = 'me'
	- z = "you"
- Concatenate and repeat strings
	- b = 'myself'
	- c = a + b
	- d = a + ' ' + b
	- silly = a \* 3

## String Operations
- len() is a function used to retrieve the length of a string in the parentheses
s =  'abc'
len(s) -> evaluates to 3
chars = len(s)

### Slicing to get ONE CHARACTER In a String

- Square brackets used to perform indexing into a string to get the value at a certain index/position
s = "abc"
s[0] -> evaluates to 'a'
s[1] -> evaluates to 'b'
s[2] -> evaluates to 'c'
s[3] -> trying to index out of bounds, error

s[-1] -> evaluates to 'c'
s[-2] -> evaluates to 'b'
s[-3] -> evaluates to 'a'

### Slicing to get a SUBSTRING

- Can slice strings using [start:stop:step]
- Get characters at start up to and including stop-1 taking every step characters

- If give two numbers, [start:stop], step=1 by default
- If give one number, you are back to indexing for the character at one location (prev slide)
- You can also omit numbers and leave just colons (try this out!)

#### Slicing Examples

- Can slice strings using [start:stop:step]
- Look at step first. +ve means go left-to-right and -ve means go right-to-left

s = 'abcdefg'

| Slicing Example | Result                                        |
| --------------- | --------------------------------------------- |
| s[3:6]          | evaluates to 'def', same as s[3:6:1]          |
| s[3:6:2]        | evaluates to 'df'                             |
| s[:]            | evaluates to 'abcdefg', same as s[0:len(s):1] |
| s[::-1]         | evaluates to 'hgfedcba'                       |
| s[4:1:-2]       | evaluates to 'ec'                             |
## Immutable Strings

- Strings are 'immutable' - cannot be modified
- You can create new objects that are versions of the original one
- Variable name can only be bound to one object

s = 'car'
s[0] = 'bar' -> throw an error
s = 'b' +s[1:len(s)] -> is allowed, s bound to new object

## Input/Output
### Printing

- Used to output stuff to console
- IN [11] : 3+2
- OUT [11] : 5
- **Command** is print
- In [12] : print(3+2)
- 5

- **Printing many objects in the same command**
	- Separate objects using commas to output them separated by spaces
	- Concatenate strings together using + to print as single object
	- a = 'the'
	- b = 3
	- c = 'musketeers'
	- print(a, b, c)
	- print(a + srt(b) + c)

### Input
- x = input(s)
	- Prints the value of the string s
	- User types in something and hits enter
	- That value is assigned to the variable x

- **Binds that value to a variable**
	- text = input("Type anything: ")
	- print(5\*text)

- input always returns an str, must cast if working with numbers
- num1 = input('Type a number: ')
- print(5\*number1)
- num2 = int(input('Type a number: '))
- print(5\*num2)

## An Important Algorithm: Newton's Method

- Finds roots of a polynomial
	- e.g., find g such that f(g, x) = g³ - x = 0

- Algorithm uses successive approximation
	- next_guess = guess - f(guess)/f'(guess)

- Partial code of algorithm that gets input and finds next guess

## F-Strings

- Available starting with Python 3.6
- Character f followed by a formatted string literal
	- Anything that can be appear in a normal string literal
	- Expressions breacketed by curly braces { }

- Expressions in curly braces evaluated at runtime, automatically converted to strings, and concatenated to the string preceding them

## Conditions for Branching

### Binding Variables and Values

- In CS, there are two notions of equal
	-  Assignment and Equality test

- `variable = value`
	- Change the stored value of variable to value
	- Nothing for us to solve, computer just does the action

- `some_expression == other_expression`
	- A test for equality
	- No binding is happening
	- Expressions are replaced by values and computer just does the comparison
	- Replaces the entire line with **True or False**

### Logical Operators on Bool

- A and b are variable names (with boolean values)
not a -> True if a is False / False if a is True
a and b -> True if both are True
a or b -> True if either or both are True

| A     | B     | A and B | A or B |
| ----- | ----- | ------- | ------ |
| True  | True  | True    | True   |
| True  | False | False   | True   |
| False | True  | False   | True   |
| False | False | False   | False  |

#### Why bool?

- When we get to flow of control, i.e. branching to different expressions based on value, we need a way of knowing if a condition is true
- E.g., if something is true, do this, otherwise do that

#### Branching in Python
```bash
if <condition\>:
	<code\>
	<code\>
	....
<rest of program\>
```

```bash
if <condition\>:
	<code\>
	<code\>
else:
	<code\>
	<code\>
	....
<rest of program\>
```

- <condition\> has a value True or False
- Indentation matters in Python!
- Do code within if block if condition is True

## Summary

- Strings provide a new data type
	- They are sequences of characters, the first one at index 0
	- They can be indexed and sliced
- Input
	- Done with the input command
	- Anything the user inputs is read as a string object!
- Output
	- Is done with the print command
	- Only objects that are printed in a .py code file will be visible in the shell
- Branching
	- Programs execute code blocks when conditions are true
	- In a if-elif-elif... structure, the first condition that is True will be executed
	- **Indentation matters in python!**