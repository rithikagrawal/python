import random


def guessFunction(guess):
    num = random.randint(1, 100)
    attempt = 1
    while (True):
        if (guess > num):
            guess = int(input("Guess another number. This one is too big: "))
            attempt += 1
        elif (guess < num):
            guess = int(input("Guess another number. This one is too small: "))
            attempt += 1
        else:
            print(
                f"Yeah!, that's the number. You guessed it in {attempt} attempts.")
            break


guess = int(input("Guess a number between 1 to 100: "))
guessFunction(guess)
