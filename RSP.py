import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("What would you choose?")
copm_choice = random.choice(item_list)

print(user_choice, copm_choice)

if user_choice == copm_choice:
    print("match tie")

elif user_choice == "Rock":
    if copm_choice == "Paper":
        print("Paper covers Rock, Computer wins")
    else:
        print("Rock smashes Scissor, You won")

elif user_choice == "Paper":
    if copm_choice == "Scissor":
        print("Scissor cuts Paper, Computer wins")
    else:
        print("Paper covers Rock, You won")

elif user_choice == "Scissors":
    if copm_choice == "Rock":
        print("Rock smashed Scissors, computer won")
    else:
        print("Scissors cuts Paper, you won")        
