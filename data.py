import sqlite3 as sql
import numpy as np

# sequence, ic50, allele
# todo: specific lengths, alleles, species && ranges for ic50 && non cystine argument

def mhc_dataset(remove_c = False, remove_u = False, remove_modes = False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns the remaining dataset in a numpy array
    """
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_modes == False:
        if remove_c == False and remove_u == False:
            c.execute('SELECT * FROM mhc_data')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT * FROM mhc_data WHERE sequence NOT LIKE \'%C%\'' +
                        'AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT * FROM mhc_data WHERE sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT * FROM mhc_data WHERE sequence NOT LIKE \'%U%\'')
    else:
        if remove_c == False and remove_u == False:
            c.execute('SELECT * FROM mhc_data')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT * FROM mhc_data WHERE inequality != \'>\' AND sequence NOT LIKE \'%C%\'' +
                        'AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT * FROM mhc_data WHERE inequality != \'>\' AND sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT * FROM mhc_data WHERE inequality != \'>\' AND sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset

def mhc_train(remove_c = False, remove_u = False, remove_modes = False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_modes == False:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_train')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_train WHERE sequence' +
                        ' NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT seqence, meas, mhc FROM mhc_train WHERE sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT seqence, meas, mhc FROM mhc_train WHERE sequence NOT LIKE \'%U%\'')
    else:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_train WHERE inequality != \'>\'')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_train WHERE inequality' +
                        ' != \'>\' AND sequence NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT seqence, meas, mhc FROM mhc_train WHERE inequality != \'>\''
                        + 'sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT seqence, meas, mhc FROM mhc_train WHERE inequality != \'>\''
                        + 'sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test1(remove_c = False, remove_u = False, remove_modes = False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_modes == False:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE sequence' +
                        'NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE sequence NOT LIKE \'%U%\'')
    else:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE inequality != \'>\' AND sequence ' +
                        'NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE inequality != \'>\' AND' +
                        ' sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test1 WHERE inequality != \'>\' AND' +
                        ' sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test2(remove_c = False, remove_u = False, remove_modes = False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect('./mhc.db')
    c = conn.cursor()
    if remove_modes == False:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE sequence' +
                        'NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE sequence NOT LIKE \'%U%\'')
    else:
        if remove_c == False and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2')
        elif remove_c == True and remove_u == True:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE inequality != \'>\' AND sequence ' +
                        'NOT LIKE \'%C%\' AND sequence NOT LIKE \'%U%\'')
        elif remove_c == True and remove_u == False:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE inequality != \'>\' AND' +
                        ' sequence NOT LIKE \'%C%\'')
        else:
            c.execute('SELECT sequence, meas, mhc FROM mhc_test2 WHERE inequality != \'>\' AND' +
                        ' sequence NOT LIKE \'%U%\'')
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]
