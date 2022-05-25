import random

# CREATOR: ARC NINJA
print("\n\n\t\t\t\tWELCOME TO GUESS THE NUMBER GAME\n")
print(
    " Description: In this game you have to guess a number from a given range of number based on your selected\n difficulty, you get a fixed amount of guesses for each difficulty and if you fail to guess the correct number\n and run out of guesses the game will end.\n Your Highscore is the least number of guesses you took to guess the correct number\n\n"
)
level = int(input("Select your difficulty between 1 - 5: " ""))
if level == 1:
    with open("Highscorelvl1.txt") as f:
        score = f.read()
        print(f"Your Previous Highscore was {score}")
    randNumber = random.randint(1, 10)
    guesses = 4
    userguess = None
    while userguess != randNumber:
        userguess = int(
            input(f"Guess a number between 1-10, you have {guesses} guesses left: " "")
        )
        guesses = guesses - 1
        if userguess == randNumber:
            print("you guessed it correctly")
        elif guesses == 0:
            print("Game Over, You Ran Out Of Guesses")
        else:
            if userguess < randNumber:
                print("your guess was lower than the number")
            elif userguess > randNumber:
                print("your guess was higher than the number")
        if guesses == 0:
            break
        else:
            None

    print(f"The number of times you guessed are {4-guesses}")

    with open("Highscorelvl1.txt", "r") as f:
        highscore = int(f.read())
    if guesses > highscore:
        print(f"You just broke the highscore, you'r new highscore is {guesses}")
        with open("Highscorelvl1.txt", "w") as f:
            f.write(str(guesses))

elif level == 2:
    with open("Highscorelvl2.txt") as f:
        score = f.read()
        print(f"Your Previous Highscore was {score}")
    randNumber = random.randint(1, 100)
    guesses = 15
    userguess = None
    while userguess != randNumber:
        userguess = int(
            input(f"Guess a number between 1-100, you have {guesses} guesses left: " "")
        )
        guesses = guesses - 1
        if userguess == randNumber:
            print("you guessed it correctly")
        elif guesses == 0:
            print("Game Over, You Ran Out Of Guesses")
        else:
            if userguess < randNumber:
                print("your guess was lower than the number")
            elif userguess > randNumber:
                print("your guess was higher than the number")
        if guesses == 0:
            break
        else:
            None

    print(f"The number of times you guessed are {15-guesses}")

    with open("Highscorelvl2.txt", "r") as f:
        highscore = int(f.read())
    if guesses > highscore:
        print(f"You just broke the highscore, you'r new highscore is {guesses}")
        with open("Highscorelvl2.txt", "w") as f:
            f.write(str(guesses))

elif level == 3:
    with open("Highscorelvl3.txt") as f:
        score = f.read()
        print(f"Your Previous Highscore was {score}")
    randNumber = random.randint(1, 500)
    guesses = 20
    userguess = None
    while userguess != randNumber:
        userguess = int(
            input(f"Guess a number between 1-500, you have {guesses} guesses left: " "")
        )
        guesses = guesses - 1
        if userguess == randNumber:
            print("you guessed it correctly")
        elif guesses == 0:
            print("Game Over, You Ran Out Of Guesses")
        else:
            if userguess < randNumber:
                print("your guess was lower than the number")
            elif userguess > randNumber:
                print("your guess was higher than the number")
        if guesses == 0:
            break
        else:
            None
    print(f"The number of times you guessed are {20-guesses}")

    with open("Highscorelvl3.txt", "r") as f:
        highscore = int(f.read())
    if guesses > highscore:
        print(f"You just broke the highscore, you'r new highscore is {guesses}")
        with open("Highscorelvl3.txt", "w") as f:
            f.write(str(guesses))

elif level == 4:
    with open("Highscorelvl4.txt") as f:
        score = f.read()
        print(f"Your Previous Highscore was {score}")
    randNumber = random.randint(1, 1000)
    guesses = 20
    userguess = None
    while userguess != randNumber:
        userguess = int(
            input(
                f"Guess a number between 1-1000, you have {guesses} guesses left: " ""
            )
        )
        guesses = guesses + 1
        if userguess == randNumber:
            print("you guessed it correctly")
        elif guesses == 0:
            print("Game Over, You Ran Out Of Guesses")
        else:
            if userguess < randNumber:
                print("your guess was lower than the number")
            elif userguess > randNumber:
                print("your guess was higher than the number")
        if guesses == 0:
            break
        else:
            None

    print(f"The number of times you guessed are {20-guesses}")

    with open("Highscorelvl4.txt", "r") as f:
        highscore = int(f.read())
    if guesses > highscore:
        print(f"You just broke the highscore, you'r new highscore is {guesses}")
        with open("Highscorelvl4.txt", "w") as f:
            f.write(str(guesses))

elif level == 5:
    with open("Highscorelvl5.txt") as f:
        score = f.read()
        print(f"Your Previous Highscore was {score}")
    randNumber = random.randint(1, 10000)
    guesses = 25
    userguess = None
    while userguess != randNumber:
        userguess = int(
            input(
                f"Guess a number between 1-10000, you have {guesses} guesses left: " ""
            )
        )
        guesses = guesses - 1
        if userguess == randNumber:
            print("you guessed it correctly")
        elif guesses == 0:
            print("Game Over, You Ran Out Of Guesses")
        else:
            if userguess < randNumber:
                print("your guess was lower than the number")
            elif userguess > randNumber:
                print("your guess was higher than the number")
        if guesses == 0:
            break
        else:
            None

    print(f"The number of times you guessed are {25-guesses}")

    with open("Highscorelvl5.txt", "r") as f:
        highscore = int(f.read())

    if guesses > highscore:
        print(f"You just broke the highscore, you'r new highscore is {guesses}")
        with open("Highscorelvl5.txt", "w") as f:
            f.write(str(guesses))

else:
    print("Please select a difficulty between 1-5 only")
