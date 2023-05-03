def is_valid_input(guessed_letter):
	guessed_letter = guessed_letter.lower()
	input_len = len(guessed_letter)

	if (input_len == 1) and (guessed_letter.isalpha()): 
		return True
	return False
    
def main():
    # Call the function func
    print(is_valid_input("$"))

if __name__ == "__main__":
    main()