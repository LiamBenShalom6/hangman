guessed_letter = input("Guess a letter: ").lower()
input_len = len(guessed_letter)
if (input_len == 1) and (guessed_letter.isalpha()):
    print(guessed_letter)
elif (guessed_letter.isalpha()) and (input_len > 1):
    print("E1")
elif  (input_len == 1) and (not(guessed_letter.isalpha())):
    print("E2")
else:
    print("E3")