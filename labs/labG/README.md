# Lab G

Exceptions

Write a program that "handles" a math error.

## Requirements:

Get the user to enter two values. They should not be converted to Int or Float when they are input.

My Input statements look like:

```py
userInput1 = input( 'enter value 1:  ' )
userInput1 = input( 'enter value 2:  ' )
```

Create a `try` block

Inside that block you need to:

1. convert the two user's inputs to Int (or Float) values
2. Create a math statement to divide the first value by the second value
3. Print the answer of that division

The code inside my `try` block looks like:

```py
value1 = int( userInput1 )
value2 = int( userInput2 )
answer = value1 // value2
print( "Your answer is:  ", answer )
```

Create an `except` block to "handle" the exception (error).

My "handler" just prints a message.

The code in my `except` block looks like:

```py
print( "Your answer did not compute" )
```

At a minimum, run your code with these inputs:

1. two non-zero numbers
2. two numbers with the first one a 0
3. two numbers with the second one a 0
4. a number and a letter
