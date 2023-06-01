from datetime import date, timedelta
import sqlite3

def list_mondays():
    start_date = date(2000, 1, 1)
    today = date.today()

    # Find the first Monday on or after the start date
    while start_date.weekday() != 0:  # 0 represents Monday
        start_date += timedelta(days=1)

    # Generate the list of Mondays
    mondays = []
    current_date = start_date
    while current_date <= today:
        mondays.append(current_date.strftime("%Y%m%d"))
        current_date += timedelta(weeks=1)

    return mondays

def get_monday_ordinal(date_str):
    if type(date_str) == str:
        return None
    else:
        date_str = str(date_str)
    year = int(date_str[:4])
    month = int(date_str[4:6])
    day = int(date_str[6:])
    input_date = date(year, month, day)
    start_date = date(2000, 1, 1)

    days_diff = (input_date - start_date).days
    monday_ordinal = days_diff // 7 + 1  # Calculate the Monday ordinal

    return monday_ordinal

# print(get_monday_ordinal('data'))
# print(get_monday_ordinal(19990815))

# #kreiranje konekcije sa bazom
# conn = sqlite3.connect('Git_atp.db')

# #kreiranje cursor objekta za izvrsavanje SQL komandi
# cursor = conn.cursor()

# conn.create_function('w',1,get_monday_ordinal)

# cursor.execute("UPDATE RANKINGS SET week = w(ranking_date)")

# conn.commit()