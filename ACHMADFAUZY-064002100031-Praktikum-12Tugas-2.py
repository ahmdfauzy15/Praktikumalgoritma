# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 20:26:44 2021
NAMA: ACHMAD FAUZY
NIM:064002100031
@author: User_PC
"""

print("PROGRAM MEMBUAT FILE MEAN DAN STD")
print("===============================================")

title = str(input("MASUKAN JUDUL FILE:"))
filename = (f"{title}.csv")
f = open(filename, "w")
f.close()
print("===============================================")
print(f"FILE {filename} TELAH DIBUAT!!")
print("TEKAN N atau n untuk menghentikan program")
print("===============================================")

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



def write(string):
    file = open(f"{title}.csv","w")
    file.write(str(string))
    file.close()
    
def read ():
    file = open(f"{title}.csv", "r")
    teks = file.read()
    print(teks)

baris = True
while baris == True:
    hasil = DATAFILE.DataFrame(data)
    print('\nLUAS DAN POPULASI NEGARA DITIAP DUNIA\n===========================================================================\n',hasil)
    print("input 1 untuk mencari dan memasukan file mean")
    print("input 2 untuk mencari dan memasukan file std ")
    print("============================================================================")
    isi = int(input("masukan pilihan:"))
    mean = hasil.groupby(['Benua']).mean()
    std = hasil.groupby(['Benua']).std()
    if isi == 0:
        print("\nTEKS TELAH TERSIMPAN")
        baris = False
    elif isi == 1:
        print('\nRata-rata data:\n',mean)
        write(mean)
        read()
    elif isi == 2:
        print('\nStandar Deviasi:\n',std)
        write(std)
        read()
