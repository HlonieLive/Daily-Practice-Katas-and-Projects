import random 

game = {
    "rock":["scissors","lizard"],
    "scissors":["lizard","paper"],
    "paper":["rock","spock"],
    "lizard":["spock","paper"],
    "spock":["rock","scissors"]
}

while True:
    user1 = input("Player1 choice: ").lower()
    cpu = random.choice(list(game.keys()))
    if user1 == "q":
        break

    while True:
        if user1 in game.keys() and cpu in game.keys():
            break
        else:
            print("Invalid input")

    if user1 == cpu:
        print(f"You chose: {user1}\nThe cpu chose: {cpu}\n\nIt's a Draw!\n\nType 'q' to quit the game!")
    elif user1 in game[cpu]:
        print(f"You chose: {user1}\nThe cpu chose: {cpu}\n\nYou loose!\n\nType 'q' to quit the game!")
    else:
        print(f"You chose: {user1}\nThe cpu chose: {cpu}\n\nYou won!\n\nType 'q' to quit the game!")

    