import math

# Exercise 2: List Comprehensions

# Create a list of integers from 1 to 20.
# Use list comprehension to create a new list containing only the even numbers from the original list.
# Use list comprehension to create a new list where each element is the square of each element from the original list.

new_list = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 19, 8, 7, 6, 5, 4, 3, 2, 1, 0]

comprehension_list = [
    element
    for element in new_list
    if element % 2 == 0
]

square_new_list = [
    int(math.pow(element,2))
    for element in new_list
]

# Feedback:

# Instead of math.pow, use the ** operator for squaring numbers.
# Using list comprehension for both cases is good practice.

# Suggested Code:
# import math

# numbers = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 19, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# even_numbers = [num for num in numbers if num % 2 == 0]
# print(even_numbers)

# squared_numbers = [num ** 2 for num in numbers]
# print(squared_numbers)
