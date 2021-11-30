"""
Created on Tue Nov 30 16:11:41 2021
NAMA: ACHMAD FAUZY
NIM: 064002100031
@author: User_PC
"""

def bubbleSort(sor):
    n = len(sor)
    for i in range(n):
        for j in range(0, n-i-1):
            if sor[j] > sor[j+1] :
                sor[j], sor[j+1] = sor[j+1], sor[j]
                
def binarySearchAppr (sor, start, end, x):
   if end >= start:
      mid = start + (end- start)//2
      if sor[mid] == x:
          return mid
      elif sor[mid] > x:
          return binarySearchAppr(sor, start, mid-1, x)
      else:
          return binarySearchAppr(sor, mid+1, end, x)
   else:
      return -1
sor = [8,2,44,55,66,75,10]
x = input("masukan angka yang dicari: ")
x = int(x)
bubbleSort(sor)
result = binarySearchAppr(sor, 0, len(sor)-1, x)
result = int(result)
print("data urut menjadi:", sor)
if result != -1:
   print ("Element is present at index "+str(result))
else:
   print ("Element is not present in array")
