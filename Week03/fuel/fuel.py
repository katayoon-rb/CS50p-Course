while True:
    try:
        X, Y = input("Enter X/Y: ").split("/")
        X, Y = int(X), int(Y)

        result = round((X / Y) * 100)

        if X > Y:
            raise TypeError()

        if result <= 1:
            result = "E"
        elif result >= 99:
            result = "F"
        else:
            result = f"{round((X / Y) * 100)}%"

    except:
        print("Try again!")
    else:
        break


print(result)
