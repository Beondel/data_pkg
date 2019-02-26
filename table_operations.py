import sqlite3 as sql
import numpy as np

def populate_mhc_test1():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT DISTINCT mhc FROM mhc_train')
    alleles = np.array([i[0] for i in c.fetchall()])

    for a in alleles:
        query = 'INSERT INTO mhc_test1 \
                 SELECT * \
                 FROM (SELECT * \
                       FROM mhc_train \
                       WHERE mhc = "{}") \
                 ORDER BY RANDOM() \
                 LIMIT (SELECT COUNT(*) \
                        FROM mhc_train \
                        WHERE mhc = "{}") / 10;'.format(a, a)
        c.execute(query)
        conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_mhc_test1()
