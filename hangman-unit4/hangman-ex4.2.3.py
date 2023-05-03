temperature = input("Insert the temperature you would like to convert: ")
type_of_temperature = temperature[-1].lower()
int_temperature = int(temperature[0:-1])
change = 0

if type_of_temperature == 'f':
    change = ((5 * int_temperature) - 160) / 9
    print(str(change) + 'C')
elif type_of_temperature == 'c':
    change = ((9 * int_temperature) + (32 * 5)) / 5
    print(str(change) + 'F')
else:
    print("you need to recognize the type!!!")