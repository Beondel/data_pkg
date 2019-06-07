import sqlite3 as sql
import numpy as np


def mhc_dataset(path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns the remaining dataset in a numpy array
    """
    conn = sql.connect(path)
    c = conn.cursor()
    query = 'SELECT * FROM mhc_data '
    if remove_c or remove_u or remove_modes:
        query = query + 'WHERE '
    if remove_c:
        query = query + 'sequence NOT LIKE \'%C%\' AND '
    if remove_u:
        query = query + 'sequence NOT LIKE \'%U%\' AND '
    if remove_modes:
        query = query + 'inequality != \'>\''
    if query.endswith('AND '):
        query = query[:-4]
    c.execute(query)
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset

def mhc_train(path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect(path)
    c = conn.cursor()
    query = 'SELECT sequence, meas, mhc FROM mhc_train '
    if remove_c or remove_u or remove_modes:
        query = query + 'WHERE '
    if remove_c:
        query = query + 'sequence NOT LIKE \'%C%\' AND '
    if remove_u:
        query = query + 'sequence NOT LIKE \'%U%\' AND '
    if remove_modes:
        query = query + 'inequality != \'>\''
    if query.endswith('AND '):
        query = query[:-4]
    c.execute(query)
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test1(path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect(path)
    c = conn.cursor()
    query = 'SELECT sequence, meas, mhc FROM mhc_test1 '
    if remove_c or remove_u or remove_modes:
        query = query + 'WHERE '
    if remove_c:
        query = query + 'sequence NOT LIKE \'%C%\' AND '
    if remove_u:
        query = query + 'sequence NOT LIKE \'%U%\' AND '
    if remove_modes:
        query = query + 'inequality != \'>\''
    if query.endswith('AND '):
        query = query[:-4]
    c.execute(query)
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def mhc_test2(path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    conn = sql.connect(path)
    c = conn.cursor()
    query = 'SELECT sequence, meas, mhc FROM mhc_test2 '
    if remove_c or remove_u or remove_modes:
        query = query + 'WHERE '
    if remove_c:
        query = query + 'sequence NOT LIKE \'%C%\' AND '
    if remove_u:
        query = query + 'sequence NOT LIKE \'%U%\' AND '
    if remove_modes:
        query = query + 'inequality != \'>\''
    if query.endswith('AND '):
        query = query[:-4]
    c.execute(query)
    dataset = np.array(c.fetchall())
    conn.close()
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]
