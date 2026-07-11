from time import sleep
from termcolor import colored


def xmas_print(string, delay):
    color = True
    for char in string:
        if char == " ":
            print(' ', end='', flush=True)
            continue
        if color:
            print(colored(char, "red"), flush=True, end='')
            color = False
            sleep(delay)
        else:
            print(colored(char, "white"), flush=True, end='')
            color = True
            sleep(delay)
    print()


def xmas_tree():
    tree = [
        "    *     ",
        "   ***    ",
        "  *****   ",
        " *******  ",
        "   | |    "
    ]
    for i in tree:
        if i == tree[-1]:
            print(colored(i, "red"))
        else:
            print(colored(i, "green"))


def main():
    xmas_tree()
    sleep(1)
    print("\n")
    xmas_print("C НОВЫМ ГОДОМ, ХОУ ХОУ ХОУ!🎅", delay=0.1)
    xmas_print("ЭТОТ ГОД БЫЛ ОЧЕНЬ ТРУДНЫМ,", delay=0.1)
    xmas_print("НО ЗАТО Я ИЗУЧИЛ...", delay=0.1)
    print(colored("ПААААААААЙТООООН 🐍", "green"))
    sleep(1)

    
main()