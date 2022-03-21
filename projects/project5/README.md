# Project 5

Calendar\
due (4/22/2019)

Develop a Python program that will generate a representation of a one month calendar.

## Requirements:

1. Get user input for which day of the week (0-6, or 1-7) the
   calendar should start on.

2. Get user input for how many days are in the month (28-31).

3. The body of the calendar should be generated with nested loops to
   generate boxes that represent each day of the month.The boxes should be in
   a grid pattern (7 across, 4-6 down). The minimum width of the interior of
   the box should be 3 characters, the minimum height should be 2 rows.

4. Each box that represents a day should have the number of that day inside the box.(Boxes that don’t represent calendar days should be empty).

5. Since this project is intended to reinforce looping and conditional processing,
   the output can be generated via text output via the

   ```py
   print( "*", end="'")
   ```

For example the boxes can be generated with the hyphen, pipe and space characters.

New lines can be generated with

```py
print()
```

Output for a calendar that starts on 5th (0 based) or 6th (1 based) day and has 28 days might look something like:

```
|----------|----------|----------|----------|----------|----------|----------|
|          |          |          |          |          |1         |2         |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|
|3         |4         |5         |6         |7         |8         |9         |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|
|10        |11        |12        |13        |14        |15        |16        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|
|17        |18        |19        |20        |21        |22        |23        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|
|24        |25        |26        |27        |28        |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|----------|----------|----------|----------|----------|----------|----------|

```
