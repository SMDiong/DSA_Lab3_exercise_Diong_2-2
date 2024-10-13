# Diong, Shan Marc C.
# BSCpE 2-2
# October 13, 2024

# Exercise 3: Provide a list comprehension that implement for a function called vowelsToUpper.

# Define the vowelsToUpper function using with list comprehension
def vowelsToUpper(user_string):
    vowels = "aeiou"
    return ''.join([ch.upper() if ch in vowels else ch for ch in user_string])


# Input the characters from the user
user_input = input("Please enter a string: ")

# Output the result
print(user_input, "==", vowelsToUpper(user_input))

# End