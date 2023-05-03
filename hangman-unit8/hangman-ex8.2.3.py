def mult_tuple(tuple1, tuple2):
    mult_tuple_t = []
    len_tuple1 = len(tuple1)
    len_tuple2 = len(tuple2)
    
    for i in range(0, len_tuple1):
        for j in range(0, len_tuple2):
                mult_tuple_t.append((tuple1[i], tuple2[j]))
    for i in range(0, len_tuple2):
        for j in range(0, len_tuple1):
                mult_tuple_t.append((tuple2[i], tuple1[j]))
    
    return tuple(mult_tuple_t)



def main():
    first_tuple = (1, 2)
    second_tuple = (4, 5)
    print(mult_tuple(first_tuple, second_tuple))

if __name__ == "__main__":
    main()