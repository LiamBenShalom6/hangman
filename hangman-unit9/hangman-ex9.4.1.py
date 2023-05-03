def choose_word(file_path, index):
    f = open(file_path, "r")
    cd_data = f.read()
    cd_splitted_lines = cd_data.split(" ")
    count_with_out_dup = 0
    
    cd_splitted_lines_with_out_dup = []
    for word in cd_splitted_lines:
        if word not in cd_splitted_lines_with_out_dup:
            count_with_out_dup += 1
            cd_splitted_lines_with_out_dup.append(word)
    index = (index - 1) % len(cd_splitted_lines)
    word_from_file = cd_splitted_lines[index]
    
    my_tuple = (count_with_out_dup, word_from_file)
    return my_tuple
        


def main():
    words_file = r"C:\Users\Liam\OneDrive\מסמכים\sigit\Python_course\Hangman\other\words.txt"
    print(choose_word(words_file, 3))
    print(choose_word(words_file, 15))

if __name__ == "__main__":
    main()