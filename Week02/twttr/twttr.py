vowel = ["a", "e", "o", "u", "i"]

input = input("Input: ").strip()
output = ""

for letter in input:
    if letter.lower() not in vowel:
        output += letter

print(f"Output: {output}")