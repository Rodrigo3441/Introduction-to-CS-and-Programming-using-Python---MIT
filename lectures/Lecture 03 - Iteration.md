
## While loops

#### Control Flow: while LOOPS

while \<condition>:
\<code>
\<code>

- \<condition> evaluates to a boolean
- if \<condition> is True, execute all the steps inside the while code block
- Check \<condition> again
- Repeat until \<condition> is False
- if \<condition> is never False, then will loop forever!!


While loops iterate through numbers in a sequence

#### Control Flow: for LOOPS

for \<variable> in \<sequence of values>:
\<code>
....

- Each time through the loop, \<variable> takes a value
- First time,  \<variable> is the first value in sequence
- Next time, \<variable> gets the second value
- etc. until \<variable> runs out of values

for n in range(5):
print(n)

- starts at 0
- next time, gets the value 1
- then, gets the value two
- ...
- etc. until gets some_num-1

## Range

- Generate a sequence of ints, following a pattern
- ``range(start, stop, step)``
	- start: first int generated
	- stop: controls last int generated (go up to but not including this int)
	- step: used to generate next int sequence

- A lot like what we saw for slicing
- Often omit start and step

- e.g., for i in range(4):
	- start defaults to 0
	- step defaults to 1
- e.g., for i in range(3,5):
	- step defaults to 1

## Summary

- Looping mechanisims
	- while and for loops
	- Lots of syntax today, be sure to get lots of practice!

- While loops
	- Loop as long as a condition is True
	- Need to make sure you don't enter an infinite loop

- For loops
	- Can loop over ranges of numbers
	- Can loop over elements of a string
	- Will soon se many other things are easy to loop over