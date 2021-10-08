"""
Created on Fri Oct  8 18:28:48 2021
@author: User_PC
NAMA: ACHMAD FAUZY
NIM: 064002100031
Tugas praktikum membuat program untuk mencari Akar Persamaan Kuadrat dan Determinan
"""

print("Quadratic Roots Finder")
print("-----------------------------")
import cmath as cm 
 
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
print("-----------------------------")
print("Persamaan kuadrat: 1x^2 + 6x + 3 = 0")    
    

if a==0:
    print("tidak valid nilai a, tidak boleh samadengan 0")
else :
    D = (b*b) - (4*a*c)
    
    if (D>0) :
       x1 = (-b + cm.sqrt(D))/(2 * a)
       x2 = (-b - cm.sqrt(D))/(2 * a)
       print("2 akar real, nilai x1 tidak sama dengan x2")
    elif D==0 :
        x1 = (-b / (2*a))
        x2 = (-b / (2*a))   
        print("2 akar real, nilai x1 sama dengan x2")  
    else :
        x1 = (-b + cm.sqrt(D))/(2 * a)
        x2 = (-b - cm.sqrt(D))/(2 * a)
        print("jenis akar immajiner")
print("DETERMINAN =", D)
print("akar x1 =" ,x1)
print("akar x2 =" ,x2)
