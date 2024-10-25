# Welcome to my GitHub page
# Project: 
# Write a program that identifies palindromic numbers from the following list and prints them in the output separated by spaces.
# Please follow my GitHub account.
# Let's get started:)))

my_list = [44, 676, 543, 983, 873, 55, 252, 909,878]

for (index, number) in enumerate(my_list, 0):
    num_to_str = str(number)
    if num_to_str == num_to_str[::-1]:
        print(f"{index}: {num_to_str}", end=" | ")