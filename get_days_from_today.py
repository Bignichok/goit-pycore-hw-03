from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        timedelta = datetime.strptime(date, "%Y-%m-%d") - datetime.now()
        return timedelta.days
    except ValueError:
        print(f"date {date} should be in appropriate format YYYY-mm-dd")

print(get_days_from_today("2021-10-09"))
print(get_days_from_today("2027-10-09"))
print(get_days_from_today("2027.10-09"))
