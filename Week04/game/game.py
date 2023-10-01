import random


while True:
    try:
        level = int(input("Level: "))
        ran = random.randint(1, level)

        while True:
            guess = int(input("Guess: "))

            if guess > ran:
                print("Too large!")

            elif guess < ran:
                print("Too small!")

            elif guess == ran:
                print("Just right!")
                raise EOFError

    except ValueError:
        pass

    except EOFError:
        break
