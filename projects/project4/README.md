# Project 4

Grid of `*` with center spot\
(due 2/26/2020)

Develop a Python program that uses nested for in loop(s) to write a series of asterisks in the shell window in the shape of a square. An additional requirement is to replace the center asterisk with an ‘O’.

## Part 1:

Use input and int functions to get a count value, from the user
that is running the program.

Create a for in loop that uses the range() function.
The loop should iterate the number of times that the user entered.

Inside the loop, add a statement to print one asterisk
and not break to the next line ( end='' ).

Run the program.You should see a single line of asterisks.
The number of asterisks should equal the number entered by the user.

At this point, when a 5 is entered, the output should look like:

```
*****
```

From here on down, the loop in Part 1 will be referenced as the Inner-Loop.

## Part 2:

Build a second for in loop to execute the loop (Inner-Loop),
that you completed in Part 1, multiple times. This new loop
is the Outer-Loop. This loop should use the range() function
to iterate through rows of asterisks. The number rows should
equal the count entered by the user.

At this point, when a 5 is entered, the output should look like:

```
*****
*****
*****
*****
*****
```

## Part 3:

To get the ‘O’ in the center … The best solutions,
that I have thought of, will replace the statement, in Part 2,
that prints the asterisk.It will replace that one statement
with an if/else structure to print an ‘O’ in the center,
or print an asterisk otherwise.

The center can be determined by the row being equal to the
midpoint and the column being equal to the midpoint.
The midpoint can be calculated as: mid = count // 2

Because the one asterisk should be in the “middle”, using odd numbers for the number of asterisks across, and the number of asterisks down, works better.

The final output, when a 5 is entered, should look like:

```
*****
*****
**O**
*****
*****
```
