# Lab D

Functions\
(due 3/4/2020)

Create a Python function that returns the multiplication of three numbers.

## Requirements:

1. You can name your function whatever you wish.

2. Your function must take in three parameters.

3. Your function must return the result of the argument values
   (parameters) multiplied together. notice it says return the result,
   not print the result


Here is an example of a Python function that _adds_ three numbers together.

```py
# define an addition function
def adder( val1, val2, val3 ) :

    desiredResult = val1 + val2 + val3

    return desiredResult
```

Your function needs to multiply, not add.

Here is an example of a Python code used to call, and test the ‘adder’ function:

```py
# call the addition function to add values together
returnedValue = adder( 3, 4, 5 )

print( "3+4+5=", returnedValue )

returnedValue = adder( 3.14, 3.14, 3.14 )

print( "3.14+3.14+3.14=", returnedValue )

returnedValue = adder( 100045, 102, 1010 )

print( "100045+102+1010=", returnedValue )
```

Please add similar code to demonstrate that your function works.
The code should be appropriately formatted and commented.
