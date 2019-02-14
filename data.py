import sqlite3 as sql
import numpy as np

def mhc_dataset():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT * FROM Data')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset