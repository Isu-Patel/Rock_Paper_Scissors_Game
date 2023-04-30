# Rock Paper Scissors Game with Python
import random

choices = ["rock", "paper", "scissors"]

print("")
print("Let's play Rock Paper ans Scissors Game.🎉")
user_choice = input("Choose 'rock', 'paper' or 'scissors' to play: ")


computer_choice = random.choice(choices)

if user_choice == computer_choice:
    print("It's a tie ❗")
elif user_choice == "rock" and computer_choice == "scissors":
    print("You Win 🎉 Rock Beats Scissors ❗")
elif user_choice == "paper" and computer_choice == "rock":
    print("You Win 🎉 Paper Folds Rock ❗")
elif user_choice == "scissors" and computer_choice == "paper":
    print("You Win 🎉 Scissors Cuts Paper ❗")
else:
    print(f"Sorry, You Lose . {computer_choice} Beats {user_choice} ❗")
