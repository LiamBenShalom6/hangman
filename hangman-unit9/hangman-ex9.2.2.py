def copy_file_content(source, destination):
    input_source_file = open(source, "r")
    input_destination_file = open(destination, "w")
    
    str_source_file = input_source_file.read()
    input_destination_file.write(str_source_file)
    
    input_destination_file.close()
    input_source_file.close()


def main():
    copy_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\copy.txt"
    paste_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\paste.txt"
    copy_file_content(copy_file, paste_file)

if __name__ == "__main__":
    main()