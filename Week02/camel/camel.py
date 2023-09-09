camelCase = input("camelCase: ").strip()
snake = ""

for letter in camelCase:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter

print(f"snake_case: {snake}")