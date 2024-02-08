"""
Part 3
Write code that asks the user to enter numbers and add them to a list only if the numbers are positive.
"""

# create an empty list to store the numbers
numbers = []
# start a while loop
while True:
    num = input("Enter a number") # get a number from the user
    if num >= "0": # check if the entered number and that it is positive
        numbers.append(int(num))# then add it to the list(what data type should the number be?)
    elif num == "":
        break# if nothing is entered stop the loop

print(numbers)# print out the list of positive number
