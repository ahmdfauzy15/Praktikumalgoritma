"""
Created on Sun Nov 21 18:46:47 2021
NAMA: ACHMAD FAUZY
NIM: 064002100031
@author: User_PC
"""
print("program membuat hasil pangkat ")
print("=====================================")
def p(x,y):
    if y <= 1:
        return x
    else:
        return p(x,y-1) * p(x,1)
    
def n(x,y):
    b = abs(y)
    hasil = float(1/p(x,b))
    return hasil 

def hasil(x,y):      
    if y == 0:
        return 1
    elif x == 0:
        return 0
    elif y > 0:
        if x > 0:
            return p(x,y)
        elif x < 0:
            return -abs(p(x,y))
    else:
        if x > 0:
            return n(x,y)
        elif x < 0:
            return -abs(n(x,y))
        
utama = int(input('bilangan utama: '))
pangkat = int(input('bilangan pangkat: '))
print("=====================================")
print('hasil',utama,"pangkat",pangkat,"adalah",hasil(utama,pangkat))
print("=====================================")
