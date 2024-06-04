# Exercise 1: Basic Set Operations

# Create a set of 5 unique integers.
# Add a new integer to the set and print the updated set.
# Try adding a duplicate integer and print the set to see what happens.
# Remove an element from the set and print the updated set.

set_var = {11, 12, 13, 14, 15}
set_var.add(8)
print(set_var)

set_var.add(11)
print(set_var)

set_var.remove(13)
print(set_var)

# Feedback:

# The code is correct and well-written.
# Consider using more descriptive variable names.

# Suggested Code:
# unique_numbers = {11, 12, 13, 14, 15}
# unique_numbers.add(8)
# print(unique_numbers)

# unique_numbers.add(11)  # Adding a duplicate does nothing
# print(unique_numbers)

# unique_numbers.remove(13)
# print(unique_numbers)