import random
def rock_paper_scissor_game():
    options = ["rock", "paper", "scissor"]
    user_value = input("Rock Paper Scissor...? :").lower()
    if user_value not in options:
        print("Invalid value :(")
        return
    computer_value = random.choice(options)
    if user_value == computer_value:
        print(f"Computer choice :{computer_value}")
        print("Its a Tie!!!")
        rock_paper_scissor_game()
    elif user_value == "rock" and computer_value == "scissor":
        print(f"Computer choice :{computer_value}")
        print("You Won!!! :)")
    elif user_value == "scissor" and computer_value == "paper":
        print(f"Computer choice :{computer_value}")
        print("You Won!!! :)")
    elif user_value == "paper" and computer_value == "rock":
        print(f"Computer choice :{computer_value}")
        print("You Won!!! :)")
    else:
        print(f"Computer choice :{computer_value}")
        print("Computer Wons!!!")
rock_paper_scissor_game()
