# Exercise 2: Tuple Unpacking

# Create a tuple with 4 elements.
# Unpack the tuple into 4 variables.
# Swap the values of the first and last variables and print the results.

tuple_var = ("name", "age", "var", "other")

first = tuple_var[0]
second = tuple_var[1]
third = tuple_var[2]
fourth = tuple_var[3]

first, fourth = fourth, first

print(first, fourth)

# Feedback:

# Tuple unpacking can be done in a single line.
# Use descriptive variable names for clarity.

# Suggested Code:

# my_tuple = ("name", "age", "var", "other")

# first, second, third, fourth = my_tuple

# first, fourth = fourth, first

# print(first, fourth)
