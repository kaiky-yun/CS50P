def main():
    amount = 50
    while amount > 0:
        print(f"Amount Due: {amount}")
        insertcoin = int(input("Insert Coin: "))
        if insertcoin == 5 or insertcoin == 10 or insertcoin == 25:
            amount = amount - insertcoin
        else:
            print("Amount Due: 50")
    amount = amount * (-1)
    print(f"Change Owed: {amount}")
main()
