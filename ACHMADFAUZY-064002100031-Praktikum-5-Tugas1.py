"""
NAMA : ACHMAD FAUZY
NIM : 064002100031
MENGHITUNG RATA RATA
"""
skor = 0    
n = list() 
ulang = 0
nomor = 0
while ulang == 0:
    nomor += 1
    x = str(input('"ENTER" untuk mengakhiri!\nNilai siswa: '))
    if not x:
        break
    else: 
        if x == 'A': 
            skor = float(4.00)
        elif x == 'A-':
            skor = float(3.75)
        elif x == 'B+':
            skor = float(3.50)
        elif x == 'B':
            skor = float(3.00)
        elif x == 'B-':
            skor = float(2.75)
        elif x == 'C+':
            skor = float(2.50)
        elif x == 'C':
            skor = float(2.00)
        elif x == 'C-':
            skor = float(1.75)
        elif x == 'D':
            skor = float(1.50)
        elif x == 'E':
            skor = float(1.25)
        else:
            print('invalid!!')
            skor = 0
            
        print(('\nNilai {0} = {1}').format(nomor,skor))
        n.append(skor)
    
rata2 = sum(n) / len(n) 
print('rata rata :', rata2)
