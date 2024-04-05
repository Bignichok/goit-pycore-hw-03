from datetime import datetime, timedelta

type User = dict[str, str]
type Users = list[User]

DATE_FORMAT = "%Y.%m.%d"

def is_weekend_day(day:int) -> bool:
    return day > 4

def get_upcoming_birthdays(users: Users) -> Users: 
    upcoming_birthdays = []
    today_date = datetime.today().date()
    
    for user in users:
        congratulation_date = None
        birthday_date = datetime.strptime(user["birthday"], DATE_FORMAT).replace(year=today_date.year).date()
        timedelta_days = (birthday_date - today_date).days

        if timedelta_days >= 0 and timedelta_days <= 7:
            weekday = birthday_date.weekday()
            if is_weekend_day(weekday):
                days_delta = 2 if weekday == 5 else 1
                congratulation_date = birthday_date + timedelta(days=days_delta)
            else:
                congratulation_date = birthday_date
        if congratulation_date:
            upcoming_birthdays.append({"name":user.get("name"), "congratulation_date": congratulation_date.strftime(DATE_FORMAT)})
        
    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Test", "birthday": "1990.04.6"},
    {"name": "Olga", "birthday": "1990.04.7"},
    {"name": "Karen", "birthday": "1990.04.8"},
    {"name": "Adam", "birthday": "1990.04.10"},
    {"name": "Sonia", "birthday": "1990.04.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
