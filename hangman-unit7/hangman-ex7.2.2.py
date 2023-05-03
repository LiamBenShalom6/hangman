def numbers_letters_count(my_str):
    count_list = []
    numbers_count = 0
    letters_count = 0
    for i in my_str:
        if i.isnumeric():
            numbers_count += 1
        else:
            letters_count += 1
    count_list.append(numbers_count)
    count_list.append(letters_count)
    return count_list
    

def main():
    print(numbers_letters_count("Python 3.6.3"))
    

if __name__ == "__main__":
    main()