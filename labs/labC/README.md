# Lab C

Loops\
(due 2/19/2019)

Use a `for in` loop to generate a multiplication table.

## Requirements:

Get user input to be used as the multiplicand in generating a
multiplication table.
Use a `for in` loop to generate the multiplier (0 through 10)
to be multiplied by the input number (multiplicand).
The code should be appropriately formatted and commented.

## Guidance:

Here are the pieces of code that I used to:
Get a value from user:

```py
multiplicand = input( 'Enter integer value: ' )
multiplicand = int( multiplicand, 10 )
```

Loop through 10 iterations:

```py
for multiplier in range(10) :
```

Calculation:

```py
result = multiplicand \* multiplier
```

Output:

```py
print( multiplicand, end='' )
print( " times ", end='' )
print( multiplier, end='' )
print( " equals ", end='' )
print( result )
```

Program output:

My output for input value 5 looks like:

```
5 times 0 equals 0
5 times 1 equals 5
5 times 2 equals 10
5 times 3 equals 15
5 times 4 equals 20
5 times 5 equals 25
5 times 6 equals 30
5 times 7 equals 35
5 times 8 equals 40
5 times 9 equals 45
```
