import re


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():
     while True:
        try:
            date = input("Date: ")


            if len(date.split("/")) == 3:
                date = date.split("/")
                M, D, Y = int(date[0]), int(date[1]), int(date[2])

                if M <= 12 and D <= 30:
                    print(f"{Y}-{makeZero(M)}-{makeZero(D)}")
                    break


            elif len(date.split(" ")):
                date = date.split(" ")

                if "," in date[1]:
                    M, D, Y = [date[0], int(re.sub(',', '', date[1])), int(date[2])]

                    if M in months and D <= 30:
                        print(f"{Y}-{makeZero(whichOne(M))}-{makeZero(D)}")
                        break

        except ValueError:
            pass

        except:
            break



def makeZero(x):
    x = "{:02d}".format(x)
    return x


def whichOne(x):
    i = 0
    while True:
        if x == months[i]:
            return i + 1

        else:
            i += 1



main()