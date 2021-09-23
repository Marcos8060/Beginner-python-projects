import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        print(guess)
        if guess < random_number:
            print("try again number is too low!!")
        elif guess > random_number:
            print("try again number is too high!!")
    print(f"congratulations you got the number {random_number} correctly")

guess(10)