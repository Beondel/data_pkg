import sqlite3 as sql
import numpy as np

# sequence, ic50, allele
# todo: specific lengths, alleles, species && ranges for ic50 && non cystine argument

def mhc_dataset(remove_c_u = False):
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_c_u == False:
        c.execute('SELECT * FROM mhc_data')
    else:
        c.execute('SELECT * FROM mhc_data WHERE sequence NOT LIKE \'%C%/\'' +
                    'AND sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset

def mhc_train(remove_c_u = False):
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_c_u == False:
        c.execute('SELECT sequence, meas, mhc FROM mhc_train')
    else:
        c.execute('SELECT seqence, meas, mhc FROM mhc_train WHERE sequence' +
                    'NOT LIKE \'%C%/\' AND sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test1(remove_c_u = False):
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_c_u == False:
        c.execute('SELECT sequence, meas, mhc FROM mhc_test1')
    else:
        c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE sequence' +
                    'NOT LIKE \'%C%/\' AND sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test2(remove_c_u = False):
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_c_u == False:
        c.execute('SELECT sequence, meas, mhc FROM mhc_test2')
    else:
        c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE sequence' +
                    'NOT LIKE \'%C%/\' AND sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]
