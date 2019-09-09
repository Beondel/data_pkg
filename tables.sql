CREATE TABLE mhc_data (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);

CREATE TABLE mhc_train (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);

CREATE TABLE mhc_test1 (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);

CREATE TABLE mhc_test2 (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);

CREATE TABLE mhc_bench (
    date VARCHAR(40),
    iedb_reference INTEGER,
    allele VARCHAR(40),
    peptide_length INTEGER,
    measurement_type VARCHAR(40),
    sequence VARCHAR(40),
    measurement_value VARCHAR(40),
    net_mhc_pan_2_8 VARCHAR(40),
    net_mhc_pan_3_0 VARCHAR(40),
    smm VARCHAR(40),
    net_mhc_3_4_ann VARCHAR(40),
    net_mhc_4_0_ann VARCHAR(40),
    arb VARCHAR(40),
    smmpmbec VARCHAR(40),
    iedb_consensus VARCHAR(40),
    net_mhc_cons VARCHAR(40),
    pickpocket VARCHAR(40),
    mhcflurry VARCHAR(40)
);
