Created on Wed Nov  3 21:02:43 2021
NAMA: ACHMAD FAUZY
NIM: 064002100031
@author: User_PC
"""
print("==============================================================")
print("program banyaknya hari dalam satu bulan sesuai tahunnya")
print("==============================================================")

def x(bulan):
    if bulan in [1,2,3,4,5,6,7,8,9,10,11,12]:
        if bulan  == 2:
            tahun = int(input("MASUKAN TAHUN : "))
            y(tahun)            
        else:
            if bulan in [1,3,5,7,8,10,12]:              
                print("ADA 31  HARI DALAM 1 BULAN INI")
                print("==============================================================")

            else:
                print("ADA 30 HARI DALAM 1 BULAN INI")
                print("==============================================================")
    else:
        print(f"Invalid masukan nilai : {bulan}")
        
def y(tahun):
    if tahun % 4 == 0:
        print("ADA 29 HARI DALAM BULAN INI")
        print("TAHUN KABISAT")
        print("==============================================================")

    else:
        print("ADA 28 HARI DALAM BULAN INI")
        print("==============================================================")
loop = True
while loop == True :
    bulan = int(input("Masukan Bulan (1-12): "))
    print("KETIK [0] UNTUK BERHENIKAN PROGRAMNYA!!!")
    if bulan == 0 :
        loop = False
        print("==============================================")
        print("TRIMAKASIH TELAH MENGISI PROGRAM INI!")
        print("==============================================")
    else:
        x(bulan)
