input_word = input("Enter a word: ").replace(" ", "").lower()
reverse_input_word = input_word[-1::-1].lower()
if input_word == reverse_input_word:
    print("OK")
else:
    print("NOT")