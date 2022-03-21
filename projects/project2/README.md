# Project 2

If, else\
(due 2/12/2020)

## Grade Calculation

Write a Python program that accepts three values from the user,
converts each to float, and stores the values in three variables.
The expected input values represent grades between 0.0 and 100.0.
The program should then sum the three grades, and store the sum
in another variable. Then the program should calculate the
numeric average of the three. After calculating the average,
the program should use Python conditional (if/elsif/else)
statements to determine and print out a final letter grade.

Get three floating point values from the user, and assign
into three variables. You can pick the names.

My first statement looks like:

```py
firstGrade = float( input( "Enter first grade:" ) )
```

1. Assign the addition of the these three variables into a
   third ‘total’ variable

2. Calculate the average of the three numbers,
   and print out the average.

3. If the average of the three numbers >= 90.0 the program
   should print the text string ‘Final grade is an A’

4. If not an ‘A’, and if the average of the three numbers >= 80.0
   the program should print the text string ‘Final grade is a B’

5. If not an ‘A’ or a ‘B’, and if the average of the three
   numbers >= 70.0 the program should print the text string
   ‘Final grade is a C’

6. If not an ‘A’, ‘B’, or a ‘C’, and if the average of the
   three numbers >= 60.0 the program should print the text
   string ‘Final grade is a D’

7. If not an ‘A’, ‘B’, ‘C’, or a ‘D’ the program should
   print the text string ‘Ooops, please work harder’

8. Use print statements to generate output to the Python Shell

9. Save your program (File menu, and “Save As” to select
   where to save your file)

10. Run your program three times (Run Menu, and “Run Module”)
    with these input values:

```
0, 0, 0
100, 100, 100
75, 65, 50
```
