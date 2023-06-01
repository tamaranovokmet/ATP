import sqlite3
import matplotlib.pyplot as plt
from datetime import date

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

# Connect to the database or create it if it doesn't exist
conn = sqlite3.connect('Git_atp.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

while True:
    u_input = input("Unesi ime, prezime igraca: ")
    if u_input == "":
        break
    ime = u_input.split(",")[0]
    ime = ime.strip()
    prezime = u_input.split(",")[1]
    prezime = prezime.strip()

    cursor.execute(f"SELECT player_id, birth_date FROM PLAYER WHERE name = '{ime}' AND last_name = '{prezime}'")
    results = cursor.fetchall()
    if len(results) > 0:
        id = results[0][0]
        birth = results[0][1] 
        id = str(id)
    else:
        print("no results ")
        continue

    # Execute the SELECT query
    query = f"SELECT week, points FROM RANKINGS WHERE player = '{id}' ORDER BY ranking_date"
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Extract x-column and y-column values from the results
    x_values = [(row[0] - get_monday_ordinal(birth)) for row in results]
    y_values = [row[1] for row in results]

    with open("x-data.txt","w") as xd:
        for x in x_values:
            xd.write(str(x)+'\n')
    xd.close()
    with open("y-data.txt","w") as yd:
        for y in y_values:
            yd.write(str(y)+'\n')
    yd.close()

    # Plot the data using Matplotlib
    plt.semilogy(x_values, y_values,label=f"{prezime}")

    
plt.xlabel('sedmica')
plt.ylabel('poeni')
plt.legend()
plt.show()

# Close the cursor and the database connection
cursor.close()
conn.close()
