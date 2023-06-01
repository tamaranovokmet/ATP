import sqlite3
import csv 


#kreiranje konekcije sa bazom
conn = sqlite3.connect('Git_atp.db')

#kreiranje cursor objekta za izvrsavanje SQL komandi

cursor = conn.cursor()

#kreiranje tabele u SQL database za smjestanje podataka iz csv-a
create_table_query = '''
CREATE TABLE IF NOT EXISTS RANKINGS (
    ranking_date int,
    rank int,
    player int,
    points int
)
'''

cursor.execute(create_table_query)


#dodajem putanju do fajla
output_file = 'joined_file.csv'


#otvaranje CSV fajla
with open(output_file, 'r') as csv_file:
    #kreiramo csv reader objekat
    csv_reader = csv.reader(csv_file)

    #citanje i printanje svakog reda fajla
    i = 0
    for row in csv_reader:
        value1 = row[0]
        value2 = row[1]
        value3 = row[2]
        value4 = row[3]

        #definisanje SQL INSERT komande
        insert_query = '''
        INSERT INTO RANKINGS (ranking_date, rank, player, points)
        VALUES (?, ?, ?, ?)
        '''

        #Execute INSERT command sa vrijednostima reda
        cursor.execute(insert_query, (value1, value2, value3, value4))

#komitovanje promjena u baze
conn.commit()

#prekidanje konekcije sa bazom
conn.close()