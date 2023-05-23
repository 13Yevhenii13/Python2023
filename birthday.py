from datetime import datetime, timedelta


def get_birthdays_per_week(users):

    start_of_week = datetime.now().date()
    end_of_week = start_of_week + timedelta(days=6)

    birthdays = {}

    for user in users:
        name = user["name"]

        birthday = user["birthday"].date()

        birthday = birthday.replace(year=start_of_week.year)

        if start_of_week.strftime("%A") == "Monday":
            end_of_week = start_of_week + timedelta(days=4)
        elif start_of_week.strftime("%A") == "Tuesday":
            end_of_week = start_of_week + timedelta(days=3)

        if start_of_week <= birthday <= end_of_week:
            birthday_day = birthday.strftime("%A")

            if birthday_day == "Saturday" or birthday_day == "Sunday":
                birthday_day = 'Monday'

            if birthday_day not in birthdays:
                birthdays[birthday_day] = []

            birthdays[birthday_day].append(name)

    for day, users in birthdays.items():
        print(f"{day}: {', '.join(users)}")


users = [
    {'name': 'Ivan', 'birthday': datetime(1995, 5, 29)},
    {'name': 'Kate', 'birthday': datetime(2002, 5, 26)},
    {'name': 'Gleb', 'birthday': datetime(1994, 5, 27)},
    {'name': 'Yevhenii', 'birthday': datetime(2004, 1, 22)},
    {'name': 'Anna', 'birthday': datetime(1998, 5, 21)},
]

get_birthdays_per_week(users)
