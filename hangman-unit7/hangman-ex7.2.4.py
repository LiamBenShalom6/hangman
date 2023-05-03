def seven_boom(end_number):
    seven_boom_list = []
    for i in range(0, end_number + 1):
        if (i % 7 == 0) or (str(i).count("7") != 0):
            seven_boom_list.append("BOOM")
        else:
            seven_boom_list.append(i)
    return seven_boom_list


def main():
    print(seven_boom(17))
    

if __name__ == "__main__":
    main()