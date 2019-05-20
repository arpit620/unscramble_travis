import os
# print(os.walk('.'))
datadir = '.'
a = [(d, folders, files) for d, folders, files in os.walk(datadir)]
print(a)