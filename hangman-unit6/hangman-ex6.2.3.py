def format_list(my_list):
    even_elements = ", ".join(my_list[::2]) # join even-indexed elements with , and space
    last_element = ", and " + my_list[-1] # add 'and' before the last element
    return even_elements + last_element

def main():
    my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"]
    # Call the function func
    new_list = format_list(my_list)
    print(new_list)

if __name__ == "__main__":
    main()