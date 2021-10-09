"""
Created on Fri Oct  8 18:28:48 2021
@author: User_PC
NAMA: ACHMAD FAUZY
NIM: 064002100031
Tugas praktikum membuat program untuk mencari Akar Persamaan Kuadrat dan Determinan
"""

print("Quadratic Roots Finder")
print("-----------------------------")
from math import sqrt

 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("-----------------------------")
print(f"Persamaan Kuadrat {a} x^2 + {b}x + {c}")

if a==0:
    print("tidak valid nilai a, tidak boleh samadengan 0")
else :
    D = (b*b) - (4*a*c)
    print("DETERMINAN" , D)
    
    if (D>0) :
       x1 = (-b + sqrt(D)) / (2 * a)
       x2 = (-b - sqrt(D)) / (2 * a)
       print(f"Akar x1 = {x1}")
       print(f"Akar x2 = {x2}")
       print("2 akar real TIDAK SAMMA , x1 tidak sama dengan x2")
       
    elif D==0 :
        x1 = (-b / (2*a))
        x2 = (-b / (2*a))   
        print("2 akar real KEMBAR , x1 sama dengan x2")  
        print(f"Akar x1 = {x1}")
        print(f"Akar x2 = {x2}")
        
    elif (D<0) :
       print("Merupakan Akar Imaginer")
       print(f"Akar x1 = -{b} + Akar {D} / {b} * {a}")
       print(f"Akar x2 = -{b} - Akar {D} / {b} * {a}")
        
