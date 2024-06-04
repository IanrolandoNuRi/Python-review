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
