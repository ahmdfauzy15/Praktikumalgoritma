"""
Created on Fri Oct 15 17:02:11 2021
NAMA: ACHMAD FAUZY
NIM: O04002100031
TUGAS looping while and for 
@author: User_PC
"""

print("program banyaknya hari dalam satu bulan sesuai tahunnya")
loop = True
while loop == True:
    print("ketik -1 untuk berhentikan program")
    month = int(input("masukan bulan (1-12) : "))
    if month == -1:
        loop = False
        print("TRIMAKASIH TELAH BERKONTRIBUSI !")
    else:
        if month in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
            if month == 2:
                year = int(input("Enter the year : "))
                if (year % 4 == 0):
                    print("ADA 29 HARI DIBULAN INI")
                else:
                    print("ADA 28 HARI DIBULAN INI")
            else:
                if month in [1, 3, 5, 7, 8, 10, 12]:
                    print("ADA 31 HARI DIBULAN INI")
                else:
                    print("ADA 30 HARI DIBULAN INI")
        else:
            print(f"eror!: {month}")
