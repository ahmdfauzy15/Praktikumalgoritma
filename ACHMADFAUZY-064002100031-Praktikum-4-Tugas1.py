"""
Created on Mon Oct 11 12:37:22 2021
NAMA: ACHMAD FAUZY
NIM: O04002100031
TUGAS looping while and for 
@author: User_PC
"""

y = int(input("nilai y: "))
for x in range(y, 0, -1):
    num = x
    for y in range(0, x):
        print(num, end=" ")
    print("\n")
    print("\r")
