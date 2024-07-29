from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
        
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    # today = date.today()
    today = string_to_date("2024.12.30")

    for user in users:
        congrates_users = []

        birthday_this_year = user["birthday"].replace(year=today.year)
        
        if birthday_this_year < today: 
            birthday_this_year = user["birthday"].replace(year=today.year + 1)
            congrates_users.append({"name": user["name"], "birthday": birthday_this_year})
            # print("new year: ",congrates_users)

        else: 
           congrates_users.append({"name": user["name"], "birthday": birthday_this_year})
           
        for user in congrates_users: 
            if 0 <= (birthday_this_year - today).days <= days:
               
                congratulation_date = adjust_for_weekend(birthday_this_year)
                congratulation_date_str = date_to_string(congratulation_date)
                upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays

# users = [
#     { "name": "1", "birthday": "1990.08.3"},
#     { "name": "6", "birthday": "1958.3.22"},
#     { "name": "6", "birthday": "1958.12.31"},
#     { "name": "J Snow", "birthday": "1990.7.31"}, 
#     { "name": "J Doe", "birthday": "1985.08.4"}
# ]

users = [
    {"name": "Bill Gates", "birthday": "1955.01.5"},
    { "name": "Steve Jobs", "birthday": "1955.12.31"},
    { "name": "Jinny Lee", "birthday": "1956.12.29"},
    { "name": "Sarah Lee", "birthday": "1957.12.28"},
    { "name": "Jonny Lee", "birthday": "1958.1.04"},
    { "name": "John Doe", "birthday": "1985.01.23"},
    { "name": "Jane Smith", "birthday": "1990.01.27"}
]

prep_users = prepare_user_list(users) 
# print("there are: ", prep_users)
res = print(get_upcoming_birthdays(prep_users, 7))