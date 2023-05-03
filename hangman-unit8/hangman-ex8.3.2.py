def main():
    mariah = {
    'first_name': 'Mariah',
    'last_name': 'Carey',
    'birth_date': '27.03.1970',
    'hobbies': ['Sing', 'Compose', 'Act']
    }

    print('Please select an option:')
    print('1. Print Maria\'s last name')
    print('2. Print the month of Maria\'s birth')
    print('3. Print the number of hobbies Maria has')
    print('4. Print Maria\'s last hobby')
    print('5. Add "Cooking" to Maria\'s hobbies')
    print('6. Print Maria\'s birth date as a tuple')
    print('7. Add Maria\'s age to the dictionary and print it')
    print('0. Exit')

    while True:
        choice = input("Enter number (1-7): ")  # get the user's choice
        
        if choice == '0':  # exit the program
            print('Goodbye!')
            break
            
        elif choice == '1':  # print Maria's last name
            print(mariah['last_name'])
            
        elif choice == '2':  # print the month of Maria's birth
            birth_date = mariah['birth_date']
            month = birth_date.split('.')[1]
            print(month)
            
        elif choice == '3':  # print the number of hobbies Maria has
            num_hobbies = len(mariah['hobbies'])
            print(num_hobbies)
            
        elif choice == '4':  # print Maria's last hobby
            last_hobby = mariah['hobbies'][-1]
            print(last_hobby)
            
        elif choice == '5':  # add "Cooking" to Maria's hobbies
            mariah['hobbies'].append('Cooking')
            print('Added "Cooking" to Maria\'s hobbies')
            
        elif choice == '6':  # print Maria's birth date as a tuple
            birth_date = mariah['birth_date']
            day, month, year = map(int, birth_date.split('.'))
            birth_date_tuple = (day, month, year)
            print(birth_date_tuple)
            
        elif choice == '7':  # add Maria's age to the dictionary and print it
            birth_date = mariah['birth_date']
            day, month, year = map(int, birth_date.split('.'))
            today = datetime.date.today()
            age = today.year - year - ((today.month, today.day) < (month, day))
            mariah['age'] = age
            print('Maria\'s age is', age)
            
        else:  # handle invalid input
            print('Invalid input. Please try again.')

if __name__ == "__main__":
    main()