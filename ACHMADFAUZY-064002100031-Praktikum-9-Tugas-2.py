# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 20:29:38 2021
NAMA: ACHMAD FAUZY
NIMM: 064002100031
@author: User_PC
"""
print("PROGRAM MEMBUAT FILE")
print("===============================================")

title = str(input("MASUKAN JUDUL FILE:"))
filename = (f"{title}.txt")
f = open(filename, "w")
f.close()
print("===============================================")
print(f"FILE {filename} TELAH DIBUAT!!")
print("TEKAN N atau n untuk menghentikan program")
print("===============================================")

def write(string):
    file = open(f"{title}.txt","w")
    file.write(str(string))
    file.close()

def read ():
    file = open(f"{title}.txt", "r")
    teks = file.read()
    print(teks)

baris = True
while baris == True:
    isi = (input(""))
    if isi == "n" or isi == "N":
        print("\nTEKS TELAH TERSIMPAN")
        baris = False
    else:
        write(isi)
        read()
