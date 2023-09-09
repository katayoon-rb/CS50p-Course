x, y, z = input("Expression: ").strip().split(" ")

if y == "+":
    a = float(x) + float(z)

elif y == "-":
    a = float(x) - float(z)

elif y == "*":
    a = float(x) * float(z)

elif y == "/":
    a = float(x) / float(z)

print(f"{a:0.1f}")
