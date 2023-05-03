def arrow(my_char, max_length):
    arrow_str = ""
    for i in range(1, max_length + 1):
        for j in range(0, i):
            arrow_str += my_char
        arrow_str += "\n"
        
    for i in range(max_length + 1, 1, -1):
        for j in range(i - 2, 0, -1):
            arrow_str += my_char
        arrow_str += "\n"
        
    return arrow_str
        
        
def main():
    print(arrow('*', 5))
    

if __name__ == "__main__":
    main()
    