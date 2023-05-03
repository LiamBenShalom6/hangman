import calendar

date = input("Enter a date, (structure - XX/XX/XXXX): ")
day = int(date[0:2])
month = int(date[3:5])
year = int(date[6:10])
day_number = calendar.weekday(year, month, day)

if day_number == 0:
    print("Monday")
elif day_number == 1:
    print("Tuesday")
elif day_number == 2:
    print("Wednesday")
elif day_number == 3:
    print("Thursday")
elif day_number == 4:
    print("Friday")
elif day_number == 5:
    print("Saturday")
elif day_number == 6:
    print("Sunday")
else:
    print("error")