def count_chars(my_str):
    my_dict = {}
    for letter in my_str:
        if not(letter in my_dict):
            my_dict[letter] = my_str.count(letter)
    return my_dict


def main():
    magic_str = "abra cadabra"
    print(count_chars(magic_str))

if __name__ == "__main__":
    main()