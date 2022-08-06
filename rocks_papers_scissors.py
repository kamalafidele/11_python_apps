import random

def play():
    user = input("'r' for rocks, 'p' for papers, 's' for scissors: ")
    computer = random.choice(['r','s','p'])

    print(f"Computer choosed: {computer}")
    if user == computer:
        return "It's a tie"
    if user != computer:
        return "You won!"
    return "You lost!"


print(play())
