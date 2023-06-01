import sqlite3
from collections import Counter
import matplotlib.pyplot as plt

# povlacenje podataka iz baze

conn = sqlite3.connect('Git_atp.db')
cursor = conn.cursor()

cursor.execute('select max_rank from PLAYER where max_rank is not null and birth_date >20000000 order by max_rank')
data = cursor.fetchall()
data = [tuple[0] for tuple in data]

cursor.close()
conn.close()

nbins= [10,20,100,1000,2015] 
# kreiranje bar charta

for nbin in nbins:
    plt.hist(data, bins=nbin)
    plt.xlabel('Max rank')
    plt.ylabel('# of players')
    plt.title(f'Distribution of players (born 2000+) by max rank with {nbin} bins')
    plt.savefig(f'C:\\Users\\W10\\Desktop\\atp\\plotovi\\Dist by max_rank(2000+),{nbin} bins.png')
    plt.close()

print("done")