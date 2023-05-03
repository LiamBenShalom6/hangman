def sort_anagrams(list_of_strings):
    list_of_lists = []
    list_in_list = []
    help_list = []
    for i in range(0, len(list_of_strings)):
        if not(list_of_strings[i] in help_list):
            help_list.append(list_of_strings[i])
            list_in_list.append(list_of_strings[i])
        else:
            continue
        for j in range(i, len(list_of_strings)):
            if i != j:
                if check_anagrams(list_of_strings[i], list_of_strings[j]):
                    list_in_list.append(list_of_strings[j])
                    help_list.append(list_of_strings[j])
        list_of_lists.append(list_in_list)
        list_in_list = []
    return list_of_lists
    
    
    
def check_anagrams(str1, str2):
    if sorted(str1) == sorted(str2):
        return True
    return False


def main():
    list_of_words = ['deltas', 'retainers', 'desalt', 'pants', 'slated', 'generating', 'ternaries', 'smelters', 'termless', 'salted', 'staled', 'greatening', 'lasted', 'resmelts']
    print(sort_anagrams(list_of_words))

if __name__ == "__main__":
    main()