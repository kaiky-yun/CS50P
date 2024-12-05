#First class - Harvard CS50

#Tell the user that this is the first code
print("First Code")

#Ask user for their name
name = input("What is your name? ")

#Say Hello to user
#\n breaks the line
print("Hello,", name + "!", "\nI'm here to help you", end="")
print(" Ok?")

# "\"" is the scape character
#To show the sep= function
print("Hello", name, sep="!!!")

# "f" in the begining of the print comand says that it is a special string
#To show the sep= function
print(f"Hello, {name}")

#Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.capitalize()

print(f"Hello, {name}")

#Same of Capitalize
name = name.title()
print(f"Helo, {name}")

#You can put everything together
name = name.title().capitalize().strip()
print(f"Helo, {name}")

#int is used for not broken number 
