# Sean Gabriel Velasco
# 8-Adelfa
# 10/20/26

score = 20

def display_intro():
    print("=================================")
    print("THREE-DOOR TREASURE HUNT")
    print("=================================")

def show_doors():
    print("Choose your door: [1] Wooden [2] Red [3] Golden")

def explore_door(choice, player):
    if choice == "1":
        print("You discovered a treasure chest!")
        print("You earned 50 points!")
        score = + 50
    elif choice == "2":
        print("Oh no! You awakened a dragon!")
        print("You lost 20 points!")
        score = - 20
    elif choice == "3":
        print("You discovered a gold key!")
        print("You earned 30 points!")
        score = + 30
    else:
        print("Invalid Door!")

def display_result(player, score):
    print(f"{player}You earned {score} points!")
    if score >= 70:
        print("TREASURE MASTER, A legendary explorer")
    elif score >= 40:
        print("BRAVE EXPLORER, A daring adventurer")
    else:
        print("BEGINNER ADVENTURER, Keep exploring!")

    print("-------- GAME RESULT --------")
    print(f"Player {player}    Starting Point: {score}")
    print(f"Total Points: {score}")
    print(f"Achievement:")

player = input("Enter your name: ")
display_intro()
print(f"Welcome to the castle, {player}!")
show_doors()
choice = input("Enter your choice: ")
explore_door(choice, player)
