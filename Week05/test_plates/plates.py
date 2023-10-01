import string

def is_valid(s):
    validated = ""
    numcheck = 0


    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in string.punctuation:
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha() and numcheck < 1:
                        validated += ch
    else:
        return False

    # Let the caller know what's up
    if validated == s:
        return True
    else:
        return False