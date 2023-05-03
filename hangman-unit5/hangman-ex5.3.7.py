def chocolate_maker(small, big, x):
    if x == 0:
        return True
    elif (small == 0) and (big == 0):
        return False
    if (x > 0):
        if (small != 0) and (big != 0):
            if chocolate_maker(small - 1, big, x - 1) or chocolate_maker(small, big - 1, x - 5):
              return True
        elif small != 0:
            if chocolate_maker(small - 1, big, x - 1):
                return True
        else:
            if chocolate_maker(small, big - 1, x - 5):
              return True
    return False
    
print(chocolate_maker(3, 1, 8))
print(chocolate_maker(3, 1, 9))
print(chocolate_maker(3, 2, 10))
