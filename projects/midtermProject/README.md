# MidTerm Project

Cross Pattern
(due during class 3/11/2020)

Develop a Python program that uses one loop within another 
loop (nested loops), to draw a pattern that looks like:

```
  *
  *
*****
  *
  *
```

The pattern is made by printing single blanks spaces
and single asterisks.

Use input and int functions to get an integer
count value, from the user that is running the program.

The loops can be either for in loops, while loops, or one of each.

It may be easier to start with a visible character instead of
a blank space. That way you can count how many are being printed.  
Once the counts are correct, you can then change it to a blank space.

The ‘inner’ loop will iterate through the number characters
across. That number will match the count value that the user entered.

The ‘outer’ loop will iterate through the number rows down.  
That number will also match the count value that the user entered.

**Hint:** you can calculate the middle of each column, and
the middle row with:

```py
middle = count // 2
```

where count is the value that the user entered.

**Hint2:** You want to print the asterisk when the inner loop is
in the middle or the outer loop is in the middle. Else you want to
print a space.
