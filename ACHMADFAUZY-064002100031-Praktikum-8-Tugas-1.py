"""
Created on Mon Nov 15 12:51:44 2021
ACHMAD FAUZY
064002100031
@author: User_PC
"""

def fibbo(n):
   if n < 0 :
       print("invalid num")
   else:
       if n == 0:
           return 0
       elif n == 1:
           return 1
       else:
           return(fibbo(n-1) + fibbo(n-2))
   
bil = int(input("masukan angka: "))
print("bilangan fibonaci dari" , bil, "adalah",fibbo(bil))
