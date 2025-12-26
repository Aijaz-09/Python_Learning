import random

options = ("rock", "paper", "scissors")
player = None
computer_score = 0
player_score = 0
while True:
    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors) (q to quit): ")
    if player.lower() == "q":
        break
    if player == "":
        print("You did not enter a choice")
    elif  options.count(player) == 0:
        print(f"{player} is not a valid choice")
    else:
        if player == "rock" and computer == "rock":
            print(f"Computer: {computer} 🪨")
            print("Tie!🤨")
        elif player == "rock" and computer == "paper":
            print(f"Computer: {computer} 📃")
            print("YOU LOSE!👎")
            computer_score += 1
        elif player == "rock" and computer == "scissors":
            print(f"Computer: {computer} ✂️")
            print("YOU WIN!👍")
            player_score += 1
        elif player == "paper" and computer == "rock":
            print(f"Computer: {computer} 🪨")
            print("YOU WIN!👍")
            player_score += 1
        elif player == "paper" and computer == "paper":
            print(f"Computer: {computer} 📃")
            print("Tie!🤨")
        elif player == "paper" and computer == "scissors":
            print(f"Computer: {computer} ✂️")
            print("YOU LOSE!👎")
            computer_score += 1
        elif player == "scissors" and computer == "rock":
            print(f"Computer: {computer} 🪨")
            print("YOU LOSE!👎")
            computer_score += 1
        elif player == "scissors" and computer == "paper":
            print(f"Computer: {computer} 📃")
            print("YOU WIN!👍")
            player_score += 1
        elif player == "scissors" and computer == "scissors":
            print(f"Computer: {computer} ✂️")
            print("Tie!🤨")

print("----------------------GAME OVER-------------------------------")
print("The scores are: ")
print("You vs Computer")
print(f"{player_score:<10}{computer_score:<10}")
if player_score > computer_score:
    print("CONGRATULATIONS!🔥🔥🔥🔥")
elif player_score < computer_score:
    print("BETTER LUCK NEXT TIME!😒😒😒😒")
else:
    print("It is a TIE!🤦‍♀️🤦‍♀️🤦‍♀️🤦‍♀️")
print("--------------------------------------------------------------")