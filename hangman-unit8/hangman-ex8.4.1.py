def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])

def pic1():
    return "  x-------x\n"\
           "  |\n"\
           "  |\n"\
           "  |\n"\
           "  |\n"\
           "  |\n"

def pic2():
    return "  x-------x\n"\
           "  |       |\n"\
           "  |       0\n"\
           "  |\n"\
           "  |\n"\
           "  |\n"

def pic3():
    return "  x-------x\n"\
           "  |       |\n"\
           "  |       0\n"\
           "  |       |\n"\
           "  |\n"\
           "  |\n"

def pic4():
    return "  x-------x\n"\
           "  |       |\n"\
           "  |       0\n"\
           "  |      /|\\\n"\
           "  |\n"\
           "  |\n"

def pic5():
    return "  x-------x\n"\
           "  |       |\n"\
           "  |       0\n"\
           "  |      /|\\\n"\
           "  |      / \n"\
           "  |\n"

def pic6():
    return "  x-------x\n"\
           "  |       |\n"\
           "  |       0\n"\
           "  |      /|\\\n"\
           "  |      / \\\n"\
           "  |\n"

HANGMAN_PHOTOS = {
    1 : pic1(),
    2 : pic2(),
    3 : pic3(),
    4 : pic4(),
    5 : pic5(),
    6 : pic6(),
}

def main():
    for num_of_tries in range(1, 7):
        print_hangman(num_of_tries)

if __name__ == "__main__":
    main()