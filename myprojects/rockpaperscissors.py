import random

choices = ["rock","paper","scissors"]

computer = random.choice(choices)
player = None


while player not in choices:
      player = input("rock, paper or scissors : ")

if player == computer:
    print("You : "+player)
    print("Computer : "+computer)
    print("You both choose the same thing")

elif player == "rock":
    if computer == "scissors":
        print("You : "+player)
        print("Computer : "+computer)
        print("You win ! ")

    if computer == "paper":
        print("You : "+player)
        print("Computer : "+computer)
        print("You lose ! ")

elif player == "paper":
    if computer == "rock":
        print("You : "+player)
        print("Computer : "+computer)
        print("You win ! ")

    if computer == "scissors":
        print("You : "+player)
        print("Computer : "+computer)
        print("You lose ! ")

elif player == "scissors":
    if computer == "rock":
        print("You : "+player)
        print("Computer : "+computer)
        print("You lose ! ")

    if computer == "paper":
        print("You : "+player)
        print("Computer : "+computer)
        print("You win ! ")



