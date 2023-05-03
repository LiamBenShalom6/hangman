replace_string = input("Please enter a string: ")
first_char = replace_string[0]
print(first_char + replace_string.replace(first_char, 'e')[1:])