import requests
import sys

api = 'https://api.coindesk.com/v1/bpi/currentprice.json'

def main ():
    print(f'${coinDesk(testInput()):,.4f}', end = "")




def testInput():
    try:
        if len(sys.argv) < 2:
            print('Missing command-line argument')
            sys.exit(1)

        elif not float(sys.argv[1]):
            print('Command-line argument is not a number')
            sys.exit(1)

        else:
            return float(sys.argv[1])


    except (TypeError, ValueError):
        print('Command-line argument is not a number')
        sys.exit(1)





def coinDesk(uinput):
    try:
        res = requests.get(api)
        a = res.json()
        b = a['bpi']['USD']['rate_float']
        c = uinput * b

    except requests.RequestException:
        print('CONNECTION ERROR!')
        sys.exit()

    return c


if __name__ == "__main__":
    main()
