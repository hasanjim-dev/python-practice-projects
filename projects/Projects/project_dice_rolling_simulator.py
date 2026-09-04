import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do You Want To Roll Again [y/n]:")
    if PlayAgain == "y":
        continue
    else:
        print("game over")
        break