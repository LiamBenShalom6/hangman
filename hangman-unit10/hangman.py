import os

MAX_TRIES = 6


def try_update_letter_guessed(guessed_letter, old_letters_guessed):

    """
    Adds a guessed letter to the old_letters_guessed list if the letter is valid, and returns True. Otherwise, prints an "X" and returns False.
    
    :param guessed_letter: A character that the user guessed
    :type guessed_letter: str
    :param old_letters_guessed: List of letters that the user guessed
    :type old_letters_guessed: list
    :return: True if the letter is valid and added to old_letters_guessed, otherwise False
    :rtype: bool
    """
    
    if check_valid_input(guessed_letter, old_letters_guessed):
        old_letters_guessed.append(guessed_letter)
        return True
    else:
        print("X")
        print(" -> ".join(sorted(old_letters_guessed)))
        return False
    
    
def check_valid_input(guessed_letter, old_letters_guessed):

    """
    Checks if a user input is valid for the hangman game. The input must be a single alphabetic character that the player has not guessed before.
    
    :param letter_guessed: A character that the user guessed
    :type letter_guessed: str
    :param old_letters_guessed: List of letters that the user guessed
    :type old_letters_guessed: list
    :return: True if the input is valid, otherwise False
    :rtype: bool
    """
    
    guessed_letter = guessed_letter.lower()
    input_len = len(guessed_letter)

    if (input_len == 1) and (guessed_letter.isalpha()): 
        return not(guessed_letter in old_letters_guessed)
    return False


def show_hidden_word(secret_word, old_letters_guessed):

    """
    Returns a string that consists of letters and underscores. 
    The string shows the letters from the old_letters_guessed list that are in the secret_word string in their appropriate position,
    and the other letters in the string (which the player has not yet guessed) as underlines.
    
    :param secret_word: The word that the user needs to guess
    :type secret_word: str
    :param old_letters_guessed: List of letters that the user guessed
    :type old_letters_guessed: list
    :return: A string that consists of letters and underscores representing the secret word
    :rtype: str
    """
    
    old_letter_with_secret_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            old_letter_with_secret_word += letter + " "
        else:
            old_letter_with_secret_word += "_ "
    return old_letter_with_secret_word


def check_win(secret_word, old_letters_guessed):

    """
    Checks if all the letters that make up the secret word are included in the list of letters that the user guessed.
    
    :param secret_word: The word that the user needs to guess
    :type secret_word: str
    :param old_letters_guessed: List of letters that the user guessed
    :type old_letters_guessed: list
    :return: True if all the letters that make up the secret word are included in the list of letters that the user guessed, otherwise False.
    :rtype: bool
    """
    
    check = True
    for letter in secret_word:
        if not(letter in old_letters_guessed):
            check = False
    return check
    
    
def print_hangman(num_of_tries):

    """"
    Prints the status of the hanging man according to the number of wrong attempts.
    :param num_of_tries: The number of wrong attempts.
    :type num_of_tries: int
    """
    
    print(HANGMAN_PHOTOS[num_of_tries])

def pic0():
    return "  x-------x\n"
    
    
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
    0 : pic0(),
    1 : pic1(),
    2 : pic2(),
    3 : pic3(),
    4 : pic4(),
    5 : pic5(),
    6 : pic6(),
}


def choose_word(file_path, index):

    """Returns a word from a text file at a specified index and the number of distinct words in the file.
    :param file_path: A string representing the path to a text file containing words separated by spaces.
    :type file_path: str
    :param index: An integer representing the position of the word to be returned in the file.
    :type index: int
    :return: A string representing the word at the specified index position in the file.
    :rtype: str
    """
        
    try:
        f = open(file_path, "r")
    except FileNotFoundError:
        print("Error: File not found")
        return None
    
    f = open(file_path, "r")
    cd_data = f.read()
    cd_splitted_lines = cd_data.split(" ")
    count_with_out_dup = 0
    
    cd_splitted_lines_with_out_dup = []
    for word in cd_splitted_lines:
        if word not in cd_splitted_lines_with_out_dup:
            count_with_out_dup += 1
            cd_splitted_lines_with_out_dup.append(word)
    index = (index - 1) % len(cd_splitted_lines)
    word_from_file = cd_splitted_lines[index]
    
    my_tuple = (count_with_out_dup, word_from_file)
    f.close()
    return word_from_file



def print_when_start():

    """
    Prints the splash screen and the maximum number of attempts.
    """
    
    print("\033[34mWelcome to the game Hangman")

    print("\033[34m", ''' 
     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/''')
                        
    print("\033[34m", MAX_TRIES, "\033[0m") # print an integer indicating how many (failed)
    # guessing attempts a player is allowed in the game.
    
    
def main():
    print_when_start()
    
    guessed_letter = ""
    
    # prompt the user to enter a file path
    file_path = input("\nEnter the path to a word file: ")

    # prompt the user to enter an index position
    index = int(input("Enter an index position (integer): "))
    
    secret_word = choose_word(file_path, index)
    
    old_letters_guessed = []
    
    num_of_tries = 0
    
    if secret_word != None:
        print("Let’s start!\n\n")
        
        print_hangman(num_of_tries)
        
        print(show_hidden_word(secret_word, old_letters_guessed))
        
        while num_of_tries < MAX_TRIES:
            guessed_letter = input("\nGuess a letter: ").lower()
            check = try_update_letter_guessed(guessed_letter, old_letters_guessed)
            while check != True: # As long as the input of the letter is invalid.
                guessed_letter = input("\nGuess a letter: ").lower()
                check = try_update_letter_guessed(guessed_letter, old_letters_guessed)
            
            if guessed_letter not in secret_word: # If the guessed_letter is not in the secret_word.
                print(":(")
                num_of_tries += 1
                print_hangman(num_of_tries)
                print(show_hidden_word(secret_word, old_letters_guessed))
            else: # If the guessed_letter is in the secret_word
                print(show_hidden_word(secret_word, old_letters_guessed))
            
            if check_win(secret_word, old_letters_guessed):
                print("\nWIN")
                break
        if num_of_tries == MAX_TRIES: # If the number of failed attempts is the maximum possible.
            print("\nLOSE")


if __name__ == "__main__":
    main()