str_to_upper = input("Please enter a string: ")
half = len(str_to_upper)//2
first_half = str_to_upper[:half]
second_half = str_to_upper[half:].upper()
print(first_half + second_half)