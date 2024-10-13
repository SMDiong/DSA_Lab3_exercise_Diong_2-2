# Diong, Shan Marc C.
# BSCpE 2-2
# October 13, 2024

# Exercise 1: From a given list of integers, create a new list using comprehension that will compute the square of odd integer elements.

# Input the maximum number from the user
max_number = int(input("Please enter the Maximum number in the list: "))

# Generate the list from the user starting with 1
number_list = list(range(1, max_number + 1))

# Compute the square of the odd numbers by using list comprehension
odd_squares = [x ** 2 for x in number_list if x % 2 != 0]

# Output the result
print("\nThe squares of all odd numbers in the list are: \n", odd_squares)

# End