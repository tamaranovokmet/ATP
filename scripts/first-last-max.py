import sqlite3
from toweeks import get_monday_ordinal as weeks

conn = sqlite3.connect('Git_atp.db')
cursor = conn.cursor()

cursor.execute("""select week,player 
                from RANKINGS,PLAYER 
                where RANKINGS.player = PLAYER.player_id 
                and (RANKINGS.player, RANKINGS.rank) in 
                (select player_id, max_rank 
                    from PLAYER 
                    where max_rank is not null 
                    and birth_date < 19900000)
                order by player""")

query_result = cursor.fetchall()

print("fetched...\n")

condensed_results = []
current_id = None
for date_id_tuple in query_result:
    if current_id == date_id_tuple[1]:
        current_tuple[0].append(date_id_tuple[0])
    else:
        if current_id != None:
            condensed_results.append(current_tuple)
        current_tuple = ([date_id_tuple[0]], date_id_tuple[1])
        current_id = current_tuple[1]
condensed_results.append(current_tuple)

print("condensed list generated...\n")

minmax_list = [] 

for tup in condensed_results:
    pid = tup[1]
    cursor.execute(f"select birth_date from PLAYER where player_id = {pid}")
    birth_week = weeks(cursor.fetchall()[0][0])
    minmax_list.append(([min(tup[0]) - birth_week, max(tup[0]) - birth_week], pid))
# print(minmax_list)

print("minmax list generated...\n")

for values in minmax_list:
    first = values[0][0]
    last = values[0][1]
    pid = values[1]
    cursor.execute(f"""UPDATE PLAYER 
                SET (first_max, last_max) = ({first},{last})
                WHERE player_id = {pid}
""")

print("done.")
conn.commit()
cursor.close()
conn.close()
