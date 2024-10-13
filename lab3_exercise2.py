# Diong, Shan Marc C.
# BSCpE 2-2
# October 13, 2024

# Exercise 2: Using comprehension, create a new list of tuples from two given lists:
# In this code, the list are made of jersey numbers with its jersey names for the game

# Input the maximum number of players in the list
max_players = int(input("Please enter the number of players in the game: "))

# Initialise the list
jersey_number = []
jersey_name = []

# Get the jersey number from the user
for i in range(max_players):
    while True:
        number = int(input(f"Please enter the number for jersey number {i+1}: "))
        if 1 <= number <= 99:
            jersey_number.append(number)
            break
        else:
            print("Invalid number! Please enter a number between 1 and 99!")

# Get the jersey name from the user
for i in range(max_players):
    name = str(input(f"Please enter the name of player number {i+1}: "))
    jersey_name.append(name)

# Generate the list by using list comprehension from the user
jersey_pair = [(jersey_number[i], jersey_name[i]) for i in range(max_players)]

# Output the result
print("The players in the game are: ", jersey_pair)

# End