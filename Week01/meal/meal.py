def main():
    sch = [
        {"meal" : "breakfast time", "start" : 7, "end" : 8},
        {"meal" : "lunch time", "start" : 12, "end" : 13},
        {"meal" : "dinner time", "start" : 18, "end" : 19}
    ]

    time = input("What time is it? ")
    time = float(convert(time))

    for d in sch:
        if time >= float(d["start"]) and time <= float(d["end"]):
            print(d["meal"])
        else:
            continue


def convert(time):
    c = 0.0
    if time.rfind(" a.m.") != -1:
        time = time.replace(" a.m.", "")
    elif time.rfind(" p.m.") != -1:
        time = time.replace(" p.m.", "")
        c = 12.0

    h, min = time.strip().split(":")
    time = float(h) + c + (float(min) / 60)
    return time


if __name__ == "__main__":
    main()