CREATE TABLE Data (
    id INTEGER PRIMARY KEY,
    species VARCHAR(40),
    mhc VARCHAR(40),
    peptide_length INTEGER,
    sequence VARCHAR(40),
    inequality CHAR(1),
    meas REAL
);
