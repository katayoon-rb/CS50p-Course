from random import randint


def main():
    level = get_level()

    i = 0
    question_dict = {}
    while i < 10:
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            solution = x + y
            question = f'{x} + {y} = '

            j = 0
            r = 0
            while j < 3:
                if r == 3:
                    print(question, solution)
                    break

                if int(input(question)) == solution:
                    break
                else:
                    print("EEE")
                    r += 1

        except ValueError:
            print("EEE")
            r += 1
            continue

        i += 1
    print(f'Score: {i}')



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 3 and level > 0:
                return level

        except ValueError:
            continue



def generate_integer(level):
    if level == 1:
        return randint(0, 9)
    if level == 2:
        return randint(10, 99)
    if level == 3:
        return randint(100, 999)



if __name__ == "__main__":
    main()
