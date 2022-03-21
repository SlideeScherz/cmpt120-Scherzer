# Project 6

Create a Tic-tac-toe board game  
due (5/13/2019)

## Requirements:

Generate a representation of a 3 by 3 grid of boxes in the
Python Shell window to be used as a Tic-tac-toe game
board. See mine output under #4.

Create a Python List to hold the status (‘X’, ‘O’, or unused).  
The list can be a one dimensional representing the boxes 0-8,
or a two dimensional representing rows 0-2 and columns 0-2.
The unused value in the array can be a blank space, ''
(empty string), None, or something else you choose.

Display a message that indicates which player’s turn it is.  
Players can be denoted as 1 or 2; X or O; or some other
notation that you derive.

Get input for the first player’s move.Entry can be row
and column, box number, or some other method that you
derive. It just needs be clear what the player is expected
to enter in order to select a specific box.

My output that demonstrates steps 1-4 looks like:

```
 | |
-----
 | |
-----
 | |

It's PlayerOne's turn,
pick a box [0-8]:
```

After getting the player’s input, the appropriate symbol
(‘X’ or ‘O’) should be displayed in the box that
matches the player’s input.

If the player selects a box that has already been selected,
a message to that effect should be displayed, and that player
should go again.

After the player’s symbol is placed in the grid, you should
switch players and repeat the steps starting at #3.

This should continue until:

1. there are three of the same symbols in any row
2. there are three of the same symbols in any column
3. there are three of the same symbols in either diagonal
4. there are no more moves allowed, because the grid is full.

On each of the conditions in #8, an appropriate message
needs to be displayed. If it is that row/column/diagonal
contain three of the same symbol, the message should include
which player is the winner.

The code should be appropriately formatted and commented

Fun Fact: the game of Tic-tac-toe is also referred to as “Noughts and Crosses”
