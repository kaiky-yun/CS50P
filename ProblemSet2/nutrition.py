def main():
    item = input("Item: ").lower()
    calories = {
        "apple": 130,
        "banana": 110,
        "grapegruit": 60,
        "honeydew": 50,
        "lemon": 15,
        "nectarine": 60,
        "peach": 60,
        "pineapple": 50,
        "strawberries": 50,
        "tangerine": 50,
        "wattermelon": 80,
        "sweetcherries": 100,
        "plums": 70,
        "pear": 100,
        "orange": 80,
        "lime": 20,
        "kiwifruit": 90,
        "grapes": 90,
        "cantaloupe": 50,
        "avocadocalifornia": 50,
    }
    if item in calories:
        print(f"Calories: {calories[item]}")



main()
