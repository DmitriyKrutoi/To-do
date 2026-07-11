from time import sleep


def kaneki_print(string, total_time):
    delay = total_time / len(string)

    for char in string:
        print(char, end='', flush=True)
        sleep(delay)
    print()


def kaneki_song():
    str_del = {
        "У меня нет проблем😎,": 2,
        "Кроме моей башки🤪.": 2,
        "1000-7😐": 1.5, 
        "Я умер, прости😈": 2.5
    }

    for string, delay in str_del.items():
        kaneki_print(string, delay)



def kaneki_countdown(): 
    i = 1000 

    while i >= 0: 
        print(f"{i} - 7 = {i - 7}") 
        i -= 7 
        sleep(0.05)

        if i - 7 < 0:
            break


def main():
    print("\033[34mЯ ДЕЕЕД ИНСАЙД\033[0m")
    sleep(1.5)
    kaneki_song()
    kaneki_countdown()


main()