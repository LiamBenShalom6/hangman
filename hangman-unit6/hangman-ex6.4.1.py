def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    input_len = len(letter_guessed)

    if (input_len == 1) and (letter_guessed.isalpha()): 
        return not(letter_guessed in old_letters_guessed)
    return False


def main():
    old_letters = ['a', 'b', 'c']
    letter_guessed = input("enter a letter_guessed: ")
    check_if_valid = check_valid_input(letter_guessed, old_letters)
    print(check_if_valid)

if __name__ == "__main__":
    main()