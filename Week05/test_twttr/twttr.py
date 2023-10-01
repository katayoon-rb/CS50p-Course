def shorten(word):
    vowel = ["a", "e", "o", "u", "i"]
    output = ""

    for letter in word:
        if letter.lower() not in vowel:
            output += letter

    return output
