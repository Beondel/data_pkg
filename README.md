# data_pkg
Package for lab data pipeline.


Database import: data.py

The purpose is to maintain separation between the dataset, the training set, the test1 set, and the test2 set.

Each method has optional parameters for:
  1) removing any amino acid sequence with "c"
      (because 'c' amino acids bond very strongly)
  2) removing any amino acid sequence with "u"
      (because 'u' amino acids bond very strongly)
  3) removing any unusual modes having to do with the frequency of the appearance of a binding affinity
      - this occurs because of max/min experimental limitations
      
Each method returns numpy array(s) representing results of a dataset from the original database
