def who_is_missing(file_name):
    input_path_file = open(file_name, "r")
    str_file = input_path_file.read()
    list_of_numbers = str_file.split(",")
    list_of_numbers[-1] = list_of_numbers[-1].replace("\n", "")
    input_write_file = open(r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\found.txt", "w")
    print(list_of_numbers)
    for i in range(1, len(list_of_numbers) + 1):
        if str(i) not in list_of_numbers:
            input_write_file.write(str(i))
            break
    input_path_file.close()
    input_write_file.close()


def main():
    find_me_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\findMe.txt"
    who_is_missing(find_me_file)

if __name__ == "__main__":
    main()