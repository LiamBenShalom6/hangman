def shift_left(my_list):
    my_list = my_list[1:] + my_list[:1]
    return my_list
    
def main():
    # Call the function
    new_list = shift_left([1, 2, 3, 10, 20])
    print(new_list)

if __name__ == "__main__":
    main()