import sqlite3 as sql
import numpy as np

# sequence, ic50, allele
# todo: specific lengths, alleles, species && ranges for ic50 && non cystine argument

def mhc_dataset():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT * FROM mhc_data')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset

def mhc_train():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT sequence, meas, mhc FROM mhc_train')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test1():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT sequence, meas, mhc FROM mhc_test1')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test2():
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    c.execute('SELECT sequence, meas, mhc FROM mhc_test2')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]
