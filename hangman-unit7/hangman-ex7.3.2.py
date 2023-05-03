def check_win(secret_word, old_letters_guessed):
    check = True
    for letter in secret_word:
        if not(letter in old_letters_guessed):
            check = False
    return check
    
    
def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(check_win(secret_word, old_letters_guessed))
    secret_word = "yes"
    old_letters_guessed = ['d', 'g', 'e', 'i', 's', 'k', 'y']
    print(check_win(secret_word, old_letters_guessed))

if __name__ == "__main__":
    main()