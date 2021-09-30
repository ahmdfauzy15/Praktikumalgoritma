"""
Created on Thu Sep 30 16:56:57 2021
@author: ACHMAD FAUZY
"""

from math import*
print("------------------------------------------------------------------------ ")
print("NAMA:ACHMAD FAUZY")
print("NIM:064002100031")
print("Latihan2_Praktikum2")
print("Membuat kalkulator jarak lingkaran besar antara dua titik di bumi")
print("------------------------------------------------------------------------ ")
print("Calculate the great circle distance between two points on the earth \n")

lat1 = int(input("Latitude 1 : "))
lat2 = int(input("Latitude 2 : "))
lon1 = int(input("Longitude 1 : "))
lon2 = int(input("Longitude 2 : "))
print("\n")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

lat1, lat2, lon1, lon2 = map(radians, [lat1, lat2, lon1, lon2])
dlon = lon2 - lon1
dlat = lat2 - lat1
a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
r = 6371
d = c*r

print(f"Jarak antara dua titik adalah {ceil(d)} km")
print("KETERANGAN: SUDAH DIBULATKAN")
print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ")
