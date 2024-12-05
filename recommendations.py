def main():
    difficult = input("Difficult or Casual? ")
    difficult = difficult.capitalize()
    if not (difficult == "Difficult" or difficult == "Casual"):
        print("Enter a valid difficulty")
        return
    
#**************************************************************************

    players = input("Multiplayer or Single-player? ")
    players = players.capitalize()
    if not (players == "Multiplayer" or players == "Single-player"):
        print("Enter a valid number of players")
        return

###########################################################################

    if difficult == "Difficult" and players == "Multiplayer":
        recommend("Poker")
    elif difficult == "Difficult" and players == "Single-player":
        recommend("Klondike")
    elif difficult == "Casual" and players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")

###########################################################################

def recommend(game):
    print("You might like", game)

main()