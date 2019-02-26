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

CREATE TABLE mch_test1 (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);

CREATE TABLE mch_test2 (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);
