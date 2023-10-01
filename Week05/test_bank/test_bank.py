from bank import value


def main():
    # print(value('Hello'))
    test_value()


def test_value():
    assert value('Hello') == 0
    assert value('Hello, Newman') == 0
    assert value('How it is going?') == 20
    assert value('How You Doing?') == 20
    assert value("What's happening?") == 100


if __name__ == "__main__":
    main()