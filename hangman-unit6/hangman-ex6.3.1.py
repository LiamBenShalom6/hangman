def are_lists_equal(list1, list2):
    list1.sort()
    list2.sort()
    return list1 == list2


def main():
    list1 = [0.6, 1, 2, 3]
    list2 = [3, 2, 0.6, 1]
    list3 = [9, 0, 5, 10.5]
    check_if_equal = are_lists_equal(list1, list2)
    print(check_if_equal)
    check_if_equal = are_lists_equal(list1, list3)
    print(check_if_equal)

if __name__ == "__main__":
    main()