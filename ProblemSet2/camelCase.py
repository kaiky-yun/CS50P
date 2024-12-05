"""
camelcase = input("camelCase: ")

def main():
    if camelcase.capitalize() == "Name":
        print("snake_case: name")
    elif camelcase.capitalize() == "Firstname":
        print("snake_case: first_name")
    else:
        print("snake_case: preferred_first_name")

"""
camelcase = input("camelCase: ")
camelcase = camelcase.capitalize()
def main():
    if camelcase == "Name":
        print("name")
    elif camelcase == "Firstname":
        print("first_name")
    else:
        print("preferred_first_name")

main()