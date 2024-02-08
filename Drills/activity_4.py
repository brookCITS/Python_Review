"""
Part 4.a
Write a program that asks the user to enter a list of names then
finds and prints the longest name in the list.

names=[]
biggest = ""
while True:
    name = input("Enter a name: ")
    if name != "":
        names.append(name)
        if len(name) > len(biggest):
            biggest = name
    else:
        break
print(names)
print(biggest)
"""
"""
Part 4.b
Edit the code from activity 2 so that it uses list Comprehension 
"""

#filted_list = [name for name in names if name[0].lower() in "aeiou"]
#print(filted_list)

even_numbers = [num for num in range(10,21) if num % 2 == 0]
print(even_numbers)

