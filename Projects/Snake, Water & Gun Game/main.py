import random as r


def game():
    user = input("Enter your choice\n s for Snake\n w for Water\n g for Gun: ")

    choices = ['s', 'w', 'g']
    comp = r.randint(0, 2)
    comp = choices[comp]

    print("Computer has choosed", comp)

    if (user == comp):
        print("Game is Tied!!")
    elif (user == 's'):
        if (comp == 'w'):
            print("You Won!!")
        else:
            print("Computer Won!")
    elif (user == 'w'):
        if (comp == 'g'):
            print("You Won!!")
        else:
            print("Computer Won!")
    elif (user == 'g'):
        if (comp == 's'):
            print("You Won!!")
        else:
            print("Computer Won!")


game()
