"""
Created on Mon Nov  1 13:04:02 2021
@author: User_PC
NAMA : ACHMAD FAUZY
NIM : 064002100031
MENGHITUNG RATA RATA
"""
def nilai_rata():
    skor = 0    
    ulang = 1
    nomor = 0
    while ulang == 1:
        nomor += 1
        x = str(input('"ENTER" untuk mengakhiri!\nNilai siswa: '))
        if x == '':
            nomor -= 1
            ulang = 0
        else:
            if x == 'A': 
                skor += float(4)
                a = '4'
            elif x == 'A-':
                skor += float(3.75)
                a = '3,75'
            elif x == 'B+':
                skor += float(3.50)
                a = '3,5'
            elif x == 'B':
                skor += float(3.00)
                a = '3'
            elif x == 'B-':
                skor += float(2.75)
                a = '2,75'
            elif x == 'C+':
                skor += float(2.50)
                a = '2,5'
            elif x == 'C':
                skor += float(2.00)
                a = '2'
            elif x == 'C-':
                skor += float(1.75)
                a = '1,75'
            else:
                print('invalidd !!!')
                nomor -= 1
                a = 'invalid number!!'
            print(f"nilai ke-{nomor} = {a}")
    rata2 = skor / nomor
    return rata2

print('rata rata:' ,nilai_rata())
