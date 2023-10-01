name = []
text = ""

while True:
    try:
        name.append(input("Name: "))

    except EOFError:
        if len(name) == 1:
            text = name[0]

        elif len(name) == 2:
            text = f"{name[0]} and {name[1]}"

        else:
            text = name[0]
            for i in name[1:-1]:
                text += f", {i}"
            text += f", and {name[len(name) - 1]}"

        print(f"\nAdieu, adieu, to {text}")
        break


