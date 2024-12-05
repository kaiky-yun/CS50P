def main():
    name = input("What's your name? ").capitalize()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()

