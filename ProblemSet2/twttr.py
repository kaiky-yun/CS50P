def main():
    text = input("Input: ")
    text = "".join([char for char in text if char.lower() not in "aeiou"])
    print(text)
main()