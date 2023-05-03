def are_files_equal(file1, file2):
    input_file1 = open(file1, "r")
    input_file2 = open(file2, "r")
    
    str_file1 = input_file1.read()
    str_file2 = input_file2.read()
    
    input_file1.close()
    input_file2.close()
    if str_file1 == str_file2:
        return True
    return False


def main():
    file1 = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\a.txt"
    file2 = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\b.txt"
    print(are_files_equal(file1, file2))

if __name__ == "__main__":
    main()