def show_hidden_word(secret_word, old_letters_guessed):
    old_letter_with_secret_word = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            old_letter_with_secret_word += letter + " "
        else:
            old_letter_with_secret_word += "_ "
    return old_letter_with_secret_word

def main():
    secret_word = "mammals"
    old_letters_guessed = ['s', 'p', 'j', 'i', 'm', 'k']
    print(show_hidden_word(secret_word, old_letters_guessed))
    

if __name__ == "__main__":
    main()