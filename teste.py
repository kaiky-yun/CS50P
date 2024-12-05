greeting = input("Greeting: ").strip()
greeting = greeting.capitalize()
if greeting.startswith("Hello"):
    print("$0")
elif greeting.startswith("H") and greeting != "Hello":
    print("$20")
else:
    print("$100")