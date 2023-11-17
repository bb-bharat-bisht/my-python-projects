import random


def play_guessing_game(x):
    random_number = random.randint(1, x)
    
    while True:
        guess = int(input(f"guess a number between 1 and {x}"))

        if guess < random_number:
            print("Sorry, guess again. Too low.")
            
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
            
        else:
            print(f"Yay! Congrats, you have guessed the right number {random_number} correctly")



play_guessing_game(10)
