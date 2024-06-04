# Exercise 1: Basic List Operations

# Create a list of 10 random integers.
# Print the list.
# Sort the list in ascending order and print it.
# Append a new integer to the list and print the updated list.
# Remove the third element from the list and print the updated list.

new_list = [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
print(f'{new_list}')
new_list.sort()
print(f'{new_list}')
new_list.append(99)
print(f'{new_list}')
new_list.remove(2)
print(f'{new_list}')

# Feedback:

# The code is correct and well-structured.
# Consider using more descriptive variable names.
# Using print(new_list) is sufficient without f-string formatting for simplicity.

# Suggested Code:
# numbers = [0, 8, 2, 6, 4, 5, 3, 7, 1, 9]
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.append(99)
# print(numbers)

# numbers.remove(2)
# print(numbers)
