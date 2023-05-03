def sequence_del(my_str):
    new_str = ""
    if len(my_str) == 0:
        return my_str
    last = my_str[0]
    new_str += last
    for i in my_str:
        if i == last:
            continue
        else:
            new_str += i
            last = i
    return new_str


def main():
    print(sequence_del("ppyyyyythhhhhooonnnnn"))
    print(sequence_del("SSSSsssshhhh"))
    print(sequence_del("Heeyyy   yyouuuu!!!"))
    

if __name__ == "__main__":
    main()