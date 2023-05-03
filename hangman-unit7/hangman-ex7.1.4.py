def squared_numbers(start, stop):
    list_of_squared = []
    while start <= stop:
        list_of_squared.append(start ** 2)
        start += 1
    return list_of_squared

def main():
    list_of_squared = squared_numbers(start=4, stop=8)
    print(list_of_squared)
    list_of_squared = squared_numbers(start=-3, stop=3)
    print(list_of_squared)

if __name__ == "__main__":
    main()
    