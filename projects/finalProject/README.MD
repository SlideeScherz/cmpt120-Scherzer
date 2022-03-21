# Final Exam Project

Develop a Python program that uses one loop within another loop
(nested loops), to draw a pattern that looks like:

```
*   *
 * *
  *
 * *
*   *
```

The pattern should be made by printing single blanks spaces and
single asterisks

Use input and int functions to get an integer count
value, from the user that is running the program.  
Use that count for width and height of the output.

The loops can be either for in loops, while loops, or one of each.

```py
count = int(input("please enter a positive integer for count: "))
middle = count // 2

for rows in range( count ) :
    for cols in range( count ) :
        if (rows==middle) or (cols==middle) :
            print( '*', end='' )
        else :
            print( ' ', end='' )
    print()
```

---

### Hint1

The diagonal the goes from the upper left corner
down to the lower right corner is when row is equal to
column. This can be the first comparison in the if
statement. A good step would be to get this diagonal working first.

### Hint2

The diagonal the goes from the upper right
corner down to the lower left corner will require some
thought. Here are two potential solutions:

The position of that asterisk can be calculated:

```py
( size - row – 1 )
```

Create another variable that starts at size-1, and gets
decremented each time through the loop

In either of these solutions you will need to add a
second comparison within the if statement, or add a
second if statement.

It may be easier to start with a visible character
instead of a blank space. That way you can count how
many are being printed. Once the counts are correct,
you can then change it to a blank space.
