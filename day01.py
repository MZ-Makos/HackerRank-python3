"""
Data Types
Declare  variables: one of type int, one of type double, and one of type String.
Read  lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your  variables.
Use the  operator to perform the following operations:
Print the sum of  plus your int variable on a new line.
Print the sum of  plus your double variable to a scale of one decimal place on a new line.
Concatenate  with the string you read as input and print the result on a new line.
"""
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i1 = 12
d1 = 4.0
s1 = 'is the best place to learn and practice coding!'

# Read and save an integer, double, and String to your variables.
i1 = int(input())
d1 = float(input())
s1 = input()

# Print the sum of both integer variables on a new line.
print(i + i1)

# Print the sum of the double variables on a new line.
print(d + d1)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + s1)


