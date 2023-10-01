import pyfiglet
import sys

try:
    if len(sys.argv) <= 2:
        text = Figlet().renderText(input("Input: "))

    elif sys.argv[1] == "-f" or sys.argv[1] == "-font":
        text = pyfiglet.Figlet(font=sys.argv[2]).renderText(input("Input: "))

except pyfiglet.FontNotFound:
    sys.exit("Invalid usage")

print(text)