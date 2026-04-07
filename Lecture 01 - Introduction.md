# Main Topics

1. Solving problems using computation
2. Python programming language
3. Organizing modular programs
4. Some simple but important algorithms
5. Algorithmic complexity

## Types of knowledge
Declarative knowledge is statements of fact
Imperative knowledge is a recipe or 'how-to'

Programming is about writing recipes to generate facts

### Numerical Example

- Square root of a number x is y such that y\*y = x
- Start with a guess, g
1. IF g\*g is close enough to x, stop and say g is the answer
2. Otherwise make a new guess by averaging g and x/g
3. Using the new guess, repeat process until close enough
- Let's try it for x = 16 and an initial guess of 3

| g      | g\*g    | x/g   | (g+x/g)/2 |
| ------ | ------- | ----- | --------- |
| 3      | 9       | 16/3  | 4.17      |
| 4.17   | 17.36   | 3.837 | 4.0035    |
| 4.0035 | 16.0277 | 3.997 | 4.000002  |
#### We have an algorithm
1. Sequence of simple steps
2. flow of control process that specifies when each step is executed
3. a means of determining when to stop

## What is a computer

Computers are machines that execute algorithms
#### Two things computers do:
- Performs simple operations 100s of billions per second!
- Remember results 100s of gigabytes of storage!
#### What kinds of calculations?
- Built-in to machine, e.g., +
- Ones that you define as the programmer

A computer will only do what you tell it to do

## Stored Program Computer

Sequence of intructions stored inside computer
- built from predefined set of primitive instructions
1. Arithmetic and logical
2. Simple tests
3. Moving data
Special program (interpreter), executes each instruction in order
- Use tests to change flow of control through sequence
- Stops when it runs out of instruction or executes a halt instruction

## Basic Primitives

Turing showed that you can compute anything with a very simple machine with only 6 primitives: left, right, print, scan, erase, no op (no operation)

Real programming languages have
- More convenient set of primitives
- Ways to combine primitives to create new primitives

Anything computable in one language is computable in any other programming language

## Where Things Go Wrong

- Syntactic erros
	- Common and easily caught
- Static semantic errors
	- Some languages check for these before running program
	- Can cause unpredictable behavior
- No linguistic errors, but different meaning that what programmer intended
	- Program crashes, stops running
	- Program runs forever
	- Program gives an answer, but it's wrong

## Objects

- Programs manipulate data objects
- Objects have a type that defines the kinds of things programs can do to them 
	- 30
		- is a number
		- We can add/sub/mult/div/exp/etc
	- 'Ana'
		- Is a sequence of characters (aka a string)
		- We can grab subtstrings, but we can't divide it by a number

#### Scalar (cannot be subdivided)
 - Numbers: 8.3, 2
 - Truth value: True, False
#### Non-scalar (have internal structure that can be accessed)
- Lists
- Dictionaries
- Sequence of characters: "abc"

## Scalar Objects

| Type     | What it means                           |
| -------- | --------------------------------------- |
| int      | represent integers, e.g. 5, -100        |
| float    | represent real numbers, e.g 3.27, 2.0   |
| bool     | represent boolean values True and False |
| NoneType | special and has one value, None         |
## Type Conversions (Casting)

- Can convert object of one type to another
	- float(3) casts the int 3 to float 3.0
	- int(3.9) casts (note the truncation) the float 3.9 to int 3
- Some operations perform implicit casts
	- round(3.9) returns the int 4

## Expressions

- Combine objects and operators to form expression
	- 3+2
	- 5/3
- An expression has a value, which has a type
	- 3+2 has value 5 and type int
	- 5/3 has value 1.6666667 and type float
-  Python evaluates expressions and stores the value. It doesn't store expressions!

- Syntax for a simple expression
	object operator object

## Variables

- Computer science variables are different than math variables
- **Math variables**
	- Abstract, e.g. (a+2 = b-1) or (x \* x = y)
	- Can represent many values

- **CS variables**
	- Is bound to one single value at a given time
	- Can be bound to an expression (but expressions evaluate to one value!), e.g. (a = b + 1) or (m = 10 and F = m\*9.98)


#### Binding Variables to Values

- In CS, the equal sign is an **assignment**
	- One value to one variable name
	- Equal sign is not equality, not "solve for x"
- An assignment binds a value to a name, e.g. pi = (355/113)

- **Step 1**: Compute the value on the right hand side (the VALUE)
	- Value stored in computer memory
- **Step 2**: Stored it (bind it) to the left hand side (the VARIABLE)
	- Retrieve value associated with name by invonking the name (typing it out)

#### Abstracting Expressions

- Why give names to values of expressions?
	- To reuse names instead of values
	- Makes code easier to read and modify
- Choose variable names wisely
	- Code needs to read
	- Today, tomorrow, next year
	- By you and others
	- You'll be fine if you stick to letters, underscores, don't start with a number
Example:

\# compute approximate value for pi
pi = 355/113
radius = 2.2
area = 2.2
circumference = pi\*(radius\*2)

**Best Code Style:**

```bash
# calculate area and circumference of a circle
# using an approximation for pi
pi = 355/113
radius = 2.2
area = pi\*(radius**2)
circumference = pi\*(radius*2)
```

## Change Bindings

- Can **re-bind** variable names using new assignment statements
- Previous value may still stored in memory but lost the handle for it
- Value for area does not change until you tell the computer to do the calculation again

## Summary

- **Objects**
	- Objects in memory have types
	- Types tell Python what operations you can do with the objects 
	- **Expressions** evaluate to one value and involve objects and operations
	- Variables bind names to objects
	- = sign is an assignment, for ex. var = type(5\*4)

- **Programs**
	- Programs only do what you tell them to do
	- Lines of code are executed in order
	- Good variable names and comments hel you read code later