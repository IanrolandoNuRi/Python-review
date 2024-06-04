# Exercise 3: Basic Tuple Operations

# Create a tuple with 5 elements: a string, an integer, a float, a list, and a dictionary.
# Access and print the second and fourth elements of the tuple.
# Try changing the third element of the tuple and observe what happens.
# Create a new tuple by concatenating the existing tuple with another tuple of 3 elements.

new_tuple = (
    "here is a story",
    3,
    2.5,
    ["first", "second"],
    {
        "element":"book",
        "pages": 524
    }
)
print(new_tuple[1],new_tuple[4])

# new_tuple[2] = 5.8

other_tuple = (
    "hello",
    "world",
    2.5,
)

result_two_tuples = new_tuple + other_tuple

# Feedback:

# The code is correct. It is good practice to avoid modifying tuples as they are immutable.
# You should print result_two_tuples to see the result of concatenation.
#
#  Suggested Code:
# my_tuple = (
#     "here is a story",
#     3,
#     2.5,
#     ["first", "second"],
#     {"element": "book", "pages": 524}
# )
# print(my_tuple[1], my_tuple[4])

# # my_tuple[2] = 5.8  # Uncommenting this will raise a TypeError

# additional_tuple = ("hello", "world", 2.5)
# combined_tuple = my_tuple + additional_tuple
# print(combined_tuple)
