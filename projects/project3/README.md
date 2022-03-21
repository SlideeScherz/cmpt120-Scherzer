# Project 3

While loops\
(due 2/20/2019)

Develop a Python program that uses while loop(s) to print a
series of asterisks to the Python Shell window.

Part one will print a single line of asterisks.

Part two will print multiple lines of asterisks.

## Part 1:

Use input and int functions to get a maximum count value,
from the user that is running the program.  
You can pick the variable name.

Create a second variable to hold an iteration count value.  
The iteration count variable will be used to control how many
times the loop executes. You can also select the name of
this variable.

Assign the iteration count variable a starting value of 0.

Write a while statement that contains a condition
(i.e. outerCount < maxCount) that will have the program continue
iterating in the while loop as long as iteration count is less
than the maximum count.

Make sure you increment the iteration count variable inside
the `while` loop, or you may end up with an endless loop.

Inside the loop add a statement to print one asterisk and
not break to the next line ( end='' )

Run the program. If you enter ‘10’, you should see 1 line
with 10 asterisks on the line.

From here on down, the loop in Part 1 will be referenced
as the Outer-Loop.

## Part 2:

Build a second (nested) while loop to control the print statement
you used that you completed in Part 1. This new loop is the
Inner-Loop. It must be indented to be 'inside' the outer loop.

You can use the same variable you created above for the
maximum count variable.

You will need another loop iteration count variable.

Set the new loop iteration variable to 0.

Outside the Inner-Loop, but inside the Outer-Loop add the statement:

```py
print()
```

This will cause a break (movement to the next line) each time
through the Outer-Loop.

Make sure you increment the new iteration count variable
(the one created in step 9) inside the Inner-Loop while loop,
or you may end up with an endless loop.

Run the program. If you enter ‘10’, you should see 10
lines with 10 asterisks on each line.
