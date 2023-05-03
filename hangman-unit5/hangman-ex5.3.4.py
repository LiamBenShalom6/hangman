def last_early(my_str):
    my_str = my_str.lower()
    if my_str[0:-1].find(my_str[-1]) == -1:
        return False
    return True
    
print(last_early("happy birthday"))
print(last_early("best of luck"))
print(last_early("Wow"))
print(last_early("X"))