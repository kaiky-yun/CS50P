name = input("What's your name? ")
name = name.capitalize()

"""
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
"""

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
#    case "Hermione":
#        print("Gryffindor")
#    case "Ron":
#        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")