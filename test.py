from data import *


x, y, z = mhc_datasets('mhc_train', './mhc.db', False, False, False)
print(x)
print(y)
print(z)
print()

x, y, z = mhc_datasets('mhc_test1', './mhc.db', False, False, False)
print(x)
print(y)
print(z)
print()

x, y, z = mhc_datasets('mhc_test2', './mhc.db', False, False, False)
print(x)
print(y)
print(z)
print()


x, y, z = mhc_datasets('mhc_bench', './mhc.db', False, False, False)
print(x)
print(y)
print(z)
print()