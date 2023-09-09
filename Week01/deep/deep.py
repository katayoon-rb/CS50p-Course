available = ["42", "forty-two", "forty two"]
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if answer in available:
    print("Yes")
else:
    print("No")