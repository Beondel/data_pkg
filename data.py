import sqlite3 as sql
import numpy as np

def mhc_datasets(table='mhc_data', path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: 'table' is the table that the data is retrieved
                  - must be 'mhc_data', 'mhc_test1', 'mhc_test2', or 'mhc_train'
                'path' is where the database is stored
                remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset
    if the table name is 'mhc_data' then will return the entire remaining dataset, otherwise,
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    if table != 'mhc_data' and table != 'mhc_train' and table != 'mhc_test1' and table != 'mhc_test2':
        raise Exception('table name ' + table + ' does not exist')
    selection = '*'
    if table != 'mhc_data':
        selection = 'sequence, meas, mhc'
    conn = sql.connect(path)
    c = conn.cursor()
    c.execute(_create_query(selection, table, remove_c, remove_u, remove_modes))
    dataset = np.array(c.fetchall())
    conn.close()
    if table == 'mhc_data':
        return dataset
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def _create_query(selection, table, remove_c, remove_u, remove_modes):
    query = 'SELECT ' + selection + ' FROM ' + table + ' '
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
    return query
