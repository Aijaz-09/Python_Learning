import random

options = ("rock", "paper", "scissors")
player = None
computer_score = 0
player_score = 0
playing = True

while playing:
    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors) (q to quit): ")
    if player.lower() == "q":
        playing = False
    if player == "":
        print("You did not enter a choice")
    elif  options.count(player) == 0:
        print(f"{player} is not a valid choice")
    else:
        print(f"Computer: {computer}")
        if player == "rock" and computer == "scissors":
            print("YOU WIN!👍")
            player_score += 1
        elif player == "paper" and computer == "rock":
            print("YOU WIN!👍")
            player_score += 1
        elif player == "scissors" and computer == "paper":
            print("YOU WIN!👍")
            player_score += 1
        elif player == computer:
            print("Tie!🤨")
        else:
            print("YOU LOSE!👎")
            computer_score += 1

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
