"""
Created on Sun Nov 14 14:20:03 2021
NNAMA: ACHMAD FAUZY
NIM: 064002100031
@author: User_PC
"""

def ordutama(x):
    per = lambda x :"(%d, '%s')" % (x,{1:"st",2:"nd",3:"rd"}.get(x if x < 20 else x % 10,"th"))
    print("PASANGAN ORDINAL NUM: "+(per(x)))
  
print("PROGRAM MEMBUAT ORDINAL NUMBER")
print("KETIKAN (0) untuk menghentikan program")
print("===============================================")
loop = True
while loop == True:
    x = int(input("Masukan Ankga : "))
    if x == 0 :
        loop = False
        print("===============================================")
        print("TRIMAKASIH,SEMOGA HARIMU MENYENANGKAN!!")
        break
    else:
        ordutama(x)
