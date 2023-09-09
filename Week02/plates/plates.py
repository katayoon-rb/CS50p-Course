import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")

    else: print("Invalid")


def is_valid(s):
    validated = ""
    numcheck = 0

    # checking the lenght
    if len(s) >= 2 and len(s) <=6 :

        # checking if the 2 first places are letters
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:

                # checking if there is a symbol
                if ch not in string.punctuation:

                    # if it was the first num, it wouldn't be 0
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch

                    # if it was another num, add it
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch

                    # if it was a letter, there wouldn't be num before
                    elif ch.isalpha() and numcheck == 0:
                        validated += ch

    if validated == s:
        return True
    else:
        return False

main()
