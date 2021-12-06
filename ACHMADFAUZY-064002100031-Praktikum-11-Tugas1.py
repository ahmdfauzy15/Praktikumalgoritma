"""
Created on Mon Dec  6 14:41:46 2021

@author: User_PC
"""

class DATA:

    jumlah = 0

    def __init__(self,nama,nim,tahun):
        self.nama = str.upper(nama)
        self.nim = str(nim)
        self.tahun = str(tahun)
        DATA.jumlah += 1

    def URUTAN(self):
        return str(f'{self.nama} ; {self.nim} ; {self.tahun}')

    def JMLHDATA(self):
        print()
        print('Nama:',self.nama)
        print('NIM:',self.nim)
        print('Tahun:',self.tahun)
        print()
        input(f'Jumlah mahasiswa sekarang adalah {DATA.jumlah} orang\nPRESS ENTER')


while True:
    print(f'\nDATA KE {(DATA.jumlah)+1}\nKetik exit untuk mengakhiri!')
    x = str(input('MASUKAN Nama: '))
    if x == 'exit':
        break
    y = str(input('MASUKA NIM: '))
    z = str(input('MASUKAN ANGKATAN: '))
    n = DATA(x,y,z)

    n.JMLHDATA()
