# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 15:21:18 2021
ACHMAD FAUZY
064002100031
@author: User_PC
"""

def bubble_sort(array):
    count = 0
    n = len(array) 
    for i in range(n): 
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                count += 1
    return array
    
    if count == 0:
        return array
    else:
        bubble_sort(array)

while True:
    while True:
        try:        
            urutkan = str(input('Masukkan angka: (1,4,7,dst)\n')).split(',')
            urutkan = [int(i) for i in urutkan]
        except:
            print('\nError:\n* Error\n* Non Bilangan-Bulat')
        else:
            break
    
    print(f'\n\nList: {urutkan}')
    
    bubble_sort(urutkan)
    
    print(f'\n\nList setelah diututkan: {urutkan}')
