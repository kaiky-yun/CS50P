def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Pricess Peach"))
"""   
    print(write_letter("Mario", "Princess Peach"))
    print(write_letter("Luigi", "Princess Peach"))
    print(write_letter("Daisy", "Princess Peach"))
    print(write_letter("Yoshi", "Princess Peach"))
"""

def write_letter(receiver, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Dear {receiver},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()