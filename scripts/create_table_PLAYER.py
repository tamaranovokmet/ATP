import sqlite3
import csv 

#kreiranje konekcije sa bazom
conn = sqlite3.connect('Git_atp.db')

#kreiranje cursor objekta za izvrsavanje SQL komandi

cursor = conn.cursor()

#kreiranje tabele u SQL database za smjestanje podataka iz csv-a
create_table_query = '''
CREATE TABLE IF NOT EXISTS PLAYER (
    player_id int,
    name varchar2(20),
    last_name varchar2(30),
    hand varchar2(1),
    birth_date int,
    country varchar2(3),
    height int
)
'''

cursor.execute(create_table_query)


#dodajem putanju do fajla
file_path = 'atp_players.csv'


#otvaranje CSV fajla
with open(file_path, 'r') as csv_file:
    #kreiramo csv reader objekat
    csv_reader = csv.reader(csv_file)

    #citanje i printanje svakog reda fajla
    i = 0
    for row in csv_reader:
        value1 = row[0]
        value2 = row[1]
        value3 = row[2]
        value4 = row[3]
        value5 = row[4]
        value6 = row[5]
        value7 = row[6]

        #definisanje SQL INSERT komande
        insert_query = '''
        INSERT INTO PLAYER (player_id, name, last_name, hand, birth_date, country, height)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''

        #Execute INSERT command sa vrijednostima reda
        cursor.execute(insert_query, (value1, value2, value3, value4, value5, value6, value7))

#komitovanje promjena u baze
conn.commit()

#prekidanje konekcije sa bazom
conn.close()