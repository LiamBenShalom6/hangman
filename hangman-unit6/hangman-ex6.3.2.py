def longest(my_list):
    max_length = max(my_list, key=len)
    return max_length
    
def main():
    list1 = ["111", "234", "2000", "goru", "birthday", "09"]
    check_if_equal = longest(list1)
    print(check_if_equal)

if __name__ == "__main__":
    main()