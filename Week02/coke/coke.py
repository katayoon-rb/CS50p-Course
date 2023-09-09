coke = 50
gain = 0

while gain < coke:
    print(f"Amount Due: {coke - gain}")

    insert = int(input("Insert Coin: ").strip())

    if insert == 25 or insert == 10 or insert == 5:
        gain += insert
    else:
        continue


print(f"Change Owed: {gain - coke}")
