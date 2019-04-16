# data_pkg
Package for lab data pipeline.

Populating the test set 1: table_operations.py

Database import: data.py (the testing file for data.py is test.py)

The purpose is to maintain separation between the dataset, the training set, the test1 set, and the test2 set.

Each method in data.py has optional parameters for:
  1) removing any amino acid sequence with "c"
      (because 'c' amino acids bond very strongly)
  2) removing any amino acid sequence with "u"
      (because 'u' amino acids bond very strongly)
  3) removing any unusual modes having to do with the frequency of the appearance of a binding affinity
      - this occurs because of max/min experimental limitations
      
Each method in data.py returns values representing results of a dataset from the original database
