class DATA:

    jumlah = 0

    def __init__(self,nama,nim,tahun):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__tahun = str(tahun)
        DATA.jumlah += 1
        
        
    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"



    def JMLHDATA(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Tahun:',self.__tahun)
        print()
        input(f'Jumlah mahasiswa sekarang adalah {DATA.jumlah} orang\nPRESS ENTER')

class gettermetod:
    jumlah = 0
    #gettermetod
    def __init__(self,nama,nim,tahun):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__tahun = str(tahun)
        DATA.jumlah += 1
        
        
    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"

    def JMLHDATA(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Tahun:',self.__tahun)
        print()
        input(f'Jumlah mahasiswa sekarang adalah {DATA.jumlah} orang\nPRESS ENTER')
    def nama(self):
        return self.__nama
    def nim(self):
        return self.__nim
    def tahun(self):
        return self.__tahun
    
class settermethod:  
    jumlah = 0
    jumlah = 0
    #gettermetod
    def __init__(self,nama,nim,tahun):
        self.__nama = str.upper(nama)
        self.__nim = str(nim)
        self.__tahun = str(tahun)
        DATA.jumlah += 1
        

    def URUTAN(self):
        return f"{self.nama} ; {self.nim} ; {self.tahun}"



    def JMLHDATA(self):
        print()
        print('Nama:',self.__nama)
        print('NIM:',self.__nim)
        print('Tahun:',self.__tahun)
        print()
        input(f'Jumlah mahasiswa sekarang adalah {DATA.jumlah} orang\nPRESS ENTER')
    #settermethod
    def nama(self, x):
        self.__nama = x
        
    def nim(self, y):
        self.__nim = y   
    
    def tahun(self,z):
        self.__(self,z)
    
    
while True:
    print("ketik 1 untuk mthod getter")
    print("ketik 2 untuk mthod getter")
    print(f'DATA KE {(DATA.jumlah)+1}\nKetik selain 1 dan 2 pada kolom pilihan method untuk mengakhiri!')
    print("==================================================================")
    method = int(input('MASUKAN pilihan (1-2): '))

    if method == 1:
        print(f'\nDATA KE {(DATA.jumlah)+1}')
        print("anda menggunaakan method getter")
        x = str(input('MASUKAN Nama: '))
        y = str(input('MASUKA NIM: '))
        z = str(input('MASUKAN ANGKATAN: '))
        n = gettermetod(x,y,z)
        n.JMLHDATA()
        print("==================================================================")

    elif method == 2:
        print(f'\nDATA KE {(DATA.jumlah)+1}')
        print("anda menggunaakan method getter")
        x = str(input('MASUKAN Nama: '))
        y = str(input('MASUKA NIM: '))
        z = str(input('MASUKAN ANGKATAN: '))
        n = settermethod(x,y,z)
        n.JMLHDATA()
        print("==================================================================")

    else :
        break
