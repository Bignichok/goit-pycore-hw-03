from datetime import datetime

def get_days_from_today(date: str) -> int:
    timedelta = datetime.strptime(date, "%Y-%m-%d") - datetime.now()
    return timedelta.days

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2027-10-09"))
