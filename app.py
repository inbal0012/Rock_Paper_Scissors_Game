import random


def get_user_input():
    while True:
        user_input = input("Choose Rock, Paper or Scissors: ").lower()
        if user_input in choices:
            return user_input
        else:
            print("Please select a valid option")


choices = ("rock", "paper", "scissors")
wins = [
    [0, 1, -1],
    [-1, 0, 1],
    [1, -1, 0]
]
keep_playing = "Y"

while keep_playing.upper() == "Y":
    comp_choice = choices[random.randrange(0, 3)]
    user_choice = get_user_input()

    comp_int = choices.index(comp_choice)
    user_int = choices.index(user_choice)

    result = wins[comp_int][user_int]
    print("\nYou have chosen: " + user_choice + " , the computer chosen: " + comp_choice)
    if result == 0:
        print("It's a tie")
    elif result == 1:
        print("You WIN!!!")
    else:
        print("You lose")

    keep_playing = input("\nDo you want to keep playing? Y/N ")


