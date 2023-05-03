def sort_prices(list_of_tuples):
    sorted_list_of_tuples = sorted(list_of_tuples, key=price)
    return sorted_list_of_tuples
    
def price(tuple_i):
    return float(tuple_i[1])
    
def main():
    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    print(sort_prices(products))

if __name__ == "__main__":
    main()