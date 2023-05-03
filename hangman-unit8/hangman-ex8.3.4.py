def inverse_dict(my_dict):
    list_in_dict = []
    reverse_dict = {}
    
    for value in my_dict.values():
        for key in my_dict.keys():
            if not(value in reverse_dict):
                if my_dict[key] == value:
                    list_in_dict.append(key)
        if list_in_dict != []:
            reverse_dict[value] = list_in_dict
        list_in_dict = []
    return reverse_dict



def main():
    course_dict = {'I': 3, 'love': 3, 'self.py!': 2}
    print(inverse_dict(course_dict))

if __name__ == "__main__":
    main()