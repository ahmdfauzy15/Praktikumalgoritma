"""
Created on Mon Nov  8 13:40:08 2021
ACHMAD FAUZY
064002100031
@author: User_PC
"""
import math

def bilangan_prima(bilangan):
    if bilangan < 1:
        return False
    rumus = math.ceil(math.sqrt(bilangan))
    
    for i in range(2,bilangan):
        if bilangan % i == 0:
            print(i,"dikali",bilangan//i,"is",bilangan)
            return False
    return True
        
def P_utama():
    if bilangan_prima(bilangan):
        print(f'{bilangan} adalah bilangan prima')
    else:
        print(f'{bilangan} bukan prima')
        
while True:
    print()
    bilangan = int(input("MASUKAN BILANGAN :"))
    P_utama()
