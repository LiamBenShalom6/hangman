def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")
    
    input_file_path = open(file_path, "r")
    str_file = input_file_path.read()
    list_of_file = str_file.split(" ")
    list_of_file_line = str_file.split("\n")
    
    if task == "sort":
        print(sorted(list_of_file))
    elif task == "rev":
        for line in list_of_file_line:
            for letter in range(len(line) - 1, 0, -1):
                print(line[letter], end="")
            print(line[0])
            
    elif task == "last":
        n = int(input("Enter a number: "))
        for line in range(len(list_of_file_line) - n, len(list_of_file_line)):
            print(list_of_file_line[line])
    else:
        print("wrong number")
    input_file_path.close()
            
        

if __name__ == "__main__":
    main()