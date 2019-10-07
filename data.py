import sqlite3 as sql
import numpy as np

def mhc_datasets(table='mhc_data', path='./mhc.db', remove_c=False, remove_u=False, remove_modes=False):
    """
    Parameters: 'table' is the table that the data is retrieved from
                  - must be 'mhc_data', 'mhc_test1', 'mhc_test2', 'mhc_train', or 'mhc_bench'
                'path' is where the database is stored
                remove every sequence with a 'c'
                remove every sequence with a 'u'
                remove the unusual modes of the dataset (not applicable for mhc_bench)
    if the table name is 'mhc_data' then will return the entire remaining dataset, otherwise,
    returns (in order): the amino acid sequences, the -log10 of binding affinities, and the alleles
    """
    if table != 'mhc_data' and table != 'mhc_train' and table != 'mhc_test1' and table != 'mhc_test2' and table != 'mhc_bench':
        raise Exception('table name ' + table + ' does not exist')
    selection = '*'
    if table != 'mhc_data' and table != 'mhc_bench':
        selection = 'sequence, meas, mhc'
    elif table == 'mhc_bench':
        selection = 'sequence, measurement_type, measurement_value, allele'
    conn = sql.connect(path)
    c = conn.cursor()
    c.execute(_create_query(selection, table, remove_c, remove_u, remove_modes))
    dataset = np.array(c.fetchall())
    conn.close()
    if table == 'mhc_data':
        return dataset
    if table == 'mhc_bench':
        return dataset.T[0], dataset.T[1], dataset.T[2].astype(float), dataset.T[3]
    return dataset.T[0], -np.log10(dataset.T[1].astype(float)), dataset.T[2]

def _create_query(selection, table, remove_c, remove_u, remove_modes):
    query = 'SELECT ' + selection + ' FROM ' + table + ' '
    if remove_c or remove_u or (remove_modes and table != 'mhc_bench'):
        query = query + 'WHERE '
    if remove_c:
        query = query + 'sequence NOT LIKE \'%C%\' AND '
    if remove_u:
        query = query + 'sequence NOT LIKE \'%U%\' AND '
    if remove_modes and table != 'mhc_bench':
        query = query + 'inequality != \'>\''
    if query.endswith('AND '):
        query = query[:-4]
    return query
