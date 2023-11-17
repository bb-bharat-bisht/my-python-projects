import random


def play_guessing_game(x):
    random_number = random.randint(1, x) #here the computer will generate number b/w given numbers.

    guess = 0  # this value kickstarts the while loop. Here, other values can also be given, we  just have to enter the loop so that we can enter somevalue initially.
    while guess != random_number:  # 0 won't be equal to anything, so will always be true.
        guess = int(input(f"guess a number between 1 and {x}"))

        if guess < random_number:
            print("Sorry, guess again. Too low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")

    print(f"Yay! Congrats, you have guessed the right number {random_number} correctly") #here we come out of the while loop, which is why we have provided the print statement outside the while loop.


play_guessing_game(10) #defining the x here. 
