# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 22:26:42 2021
NAMA: ACHMAD FAUZY
NIM: 064002100031
@author: User_PC
"""
print("program membuat binary serach")
print("==========================================")
nama = []
nim = []
file = open('mahasiswa_gasal_2021.csv','r')
jumlahdata = []
y = 0
baris = []
for line in file:
    y += 1
    baris = line.split(',')
    if y == 35:
        break
    else:
        if y == 1:
            nim.append(baris[1])
            nama.append(baris[2])
        else:
            nim.append(str(baris[1]))
            nama.append(baris[2])
nama = [line.strip() for line in nama]
file.close()
file = open('mahasiswa_gasal_2021.csv','r')
data2 = []
x = 0
for line in file:
    data2.append(line)
    x+=1
    if x >= 34:
        break
    else:
        pass    
file.close()

def unama(x,y):
    m = (len(x)-1) // 2
    
    if x[m] == y:
        return m
  
    l = 0
    while True:
        if x[l] == y:
            return l
        elif l == m:
            break
        else:
            l += 1
  
    l = (len(y)-1)
    while True:
        try:
            if x[l] == y:
                return l
            elif l == m:
                break
            else:
                l -= 1
        except IndexError:
            return -1
    return -1
    
def utknomor(arr, l, r, x):
 
    if r >= l:
 
        mid = l + (r - l) // 2

        if mid == x:
            return mid

        elif mid > x:
            return utknomor(arr, l, mid-1, x)

        else:
            return utknomor(arr, mid + 1, r, x)
 
    else:
        return -1
    
while True:

    opsi = str.lower(input('masukan opsion \nA. INPUT NAMA \nB. INPUT NIM \nPILIH OPSI A atau B??'))
    if opsi == 'a':
        cari = str.upper(input('masukan data: '))
        result = unama(nama,cari)
        if result == -1:
            print('INVALID NUM!!!')
        else:
            print(data2[result])
    else:
        opsi == 'b'
        try:
            cari = str(input('masukan data: '))
            if cari[0] == '0':
                caril = list(cari)
                caril.remove(caril[0])
                cari = ''.join(caril)
        except ValueError:
            print('INVALID NUM!!')
        else:
            result = unama(nim,cari)
            if result == -1:
                print('INVALID NUM!!')
            else:
                print('>>',data2[result])
