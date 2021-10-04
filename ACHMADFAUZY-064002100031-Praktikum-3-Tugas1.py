"""
Created on Mon Oct  4 13:04:55 2021
@author: User_PC
"""

print("------------------------------------------------")
print("NAMA:ACHMAD FAUZY")
print("NIM:064002100031")
print("------------------------------------------------")

print("Jenis segiiga")
print("------------------------------------------------")

a = int(input("sisi A :"))
b = int(input("sisi B :"))
c = int(input("sisi C :"))

if a == b == c :
    print(" jenis segitiga sama sisi")
elif a + b <= c or a + c <= b or b + c <= a  :
     print("bukan jenis segitiga ")
elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a :
    print("jenis segitiga siku siku")
elif a == b or a == c or b == c :
    print("jenis segitiga sama kaki")
else :
    print(" segitiga sembarang ")
