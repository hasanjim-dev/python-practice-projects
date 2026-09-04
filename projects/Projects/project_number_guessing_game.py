# import random
# randomNumber = random.randrange(1,200)
# userinput = int(input("Guess the number:"))
#
# if userinput > randomNumber:
#     print(f"Random Number is {randomNumber}")
#     print(f"The number {userinput} is higher than the number {randomNumber}")
# elif userinput < randomNumber:
#     print(f"Random Number is {randomNumber}")
#     print(f"The number {userinput} is lower than the number {randomNumber}")
# else :
#     print(f"Random Number is {randomNumber}")
#     print("congratulations! you guessed the correct number")

import random

def play_game():
    print("\n=== NUMBER GUESSING GAME ===")
    print("Select Difficulty:")
    print("1. Easy (1-50, 10 chances)")
    print("2. Medium (1-100, 7 chances)")
    print("3. Hard (1-200, 5 chances)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        max_num = 50
        max_attempts = 10
    elif choice == "2":
        max_num = 100
        max_attempts = 7
    else:
        max_num = 200
        max_attempts = 5

    randomNumber = random.randint(1, max_num)
    attempts = 0
    guessed = False

    print(f"\nI'm thinking of a number between 1 and {max_num}")
    print(f"You have {max_attempts} chances to guess it!\n")

    while attempts < max_attempts:
        try:
            userinput = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number: "))
            attempts += 1

            if userinput < 1 or userinput > max_num:
                print(f"Please enter a number between 1 and {max_num}")
                continue

            if userinput > randomNumber:
                diff = userinput - randomNumber
                if diff > 20:
                    print("Too high!")
                else:
                    print("A little high!")

            elif userinput < randomNumber:
                diff = randomNumber - userinput
                if diff > 20:
                    print("Too low!")
                else:
                    print("A little low!")

            else:
                print(f"\n🎉 Congratulations! You guessed it in {attempts} attempts!")
                print(f"The number was {randomNumber}")
                score = (max_attempts - attempts + 1) * 10
                print(f"Your score: {score} points! ")
                guessed = True
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    if not guessed:
        print(f"\n Game Over! The number was {randomNumber}")
        print("Better luck next time!")

while True:
    play_game()
    play_again = input("\nPlay again? (y/n):").lower()
    if play_again != 'y':
        print("\nThanks for playing! ")
        break