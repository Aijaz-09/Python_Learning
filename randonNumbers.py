import random
from random import randint

low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# number = random.randint(low,high)
# number = random.random()  #For floating point number
# option = random.choice(options)
random.shuffle(cards)
print(cards)