"""
Created on Tue Dec 14 22:27:02 2021
NAMA:ACHMAD FAUZY
NIM:064002100031
@author: user_pc
"""

file = open('Negara.csv','r')

class my_dictionary(dict):

    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

data = my_dictionary()
c1 = []
c2 = []
c3 = []
c4 = []
c5 = []

x = 0
for cache in file:
    x += 1
    cache = cache.split(',')
    if x == 1:
        pass
    else:
        p1 = cache[0]
        c1.append(p1)
        p2 = cache[1]
        c2.append(p2)
        p3 = cache[2]
        c3.append(p3)
        p4 = int(cache[3])
        c4.append(p4)
        p5 = int(cache[4])
        c5.append(p5)

data.add('Negara',c1)
data.add("Ibu Kota",c2)
data.add('Benua',c3)
data.add('Luas',c4)
data.add('Populasi',c5)

import pandas as DATAFILE

hasil = DATAFILE.DataFrame(data)

print('\nLUAS DAN POPULASI NEGARA DITIAP DUNIA\n===========================================================================\n',hasil)


mean = hasil.groupby(['Benua']).mean()
std = hasil.groupby(['Benua']).std()
print("============================================================================")
print('\nRata-rata data:\n',mean)
print("============================================================================")
print('\nStandar Deviasi:\n',std)
