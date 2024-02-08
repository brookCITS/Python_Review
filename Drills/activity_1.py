# Part 1
# What does the following code do? Add a comment to each line of code

names = []   #creating a new list
while True:   #starting a while loop
    answer = input("Enter a name: ")  #ask the user for their name
    if answer != "": #conditional to check if the user typed a name
        names.append(answer) #add the name to the list
    else:
        break #stops the loop
print(names)  #printing the list of names