def extend_list_x(list_x, list_y):
    list_x = [*list_y, *list_x]
    return list_x

def main():
    x = [4, 5, 6]
    y = [1, 2, 3]
    new_list = extend_list_x(x, y)
    print(new_list)

if __name__ == "__main__":
    main()