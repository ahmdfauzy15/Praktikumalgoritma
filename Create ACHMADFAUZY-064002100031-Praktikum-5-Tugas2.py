"""
Created on Fri Oct 22 13:17:58 2021
NAMA: ACHMAD FAUZY
NIM: 064002100031
MEMBUAT TIKET KEBUN BINATANG MENGUNAKAN PEMOGRAMAN
@author: User_PC
"""
print("""
====================================
HARGA TIKET ZOO PLANET
====================================
1. UMUR 1-2 TAHUN : GRATIS!
2. UMUR 3-12 TAHUN : $14.OO
3. UMUR 13-64 TAHUN :  $23.00
4. UMUR 64 TAHUN KEATAS : $18.00
====================================
TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI !!
      """)
jumlahUang = 0
while True:
 
    try:
        umur = int(input("SILAKAN MASUKAN UMUR: "))
    except ValueError:
        break
    if umur <= 2:
        jumlahUang += 0
        print("==========================================================")
        print("HARGA TIKET GRATIS UNTUK UMUR 2 TAHUN KEBAWAH")
        print(f"TOTAL HARGA SAAT INI : ${jumlahUang}")
        print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
        print("==========================================================")

    elif umur in [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        jumlahUang += 14.00
        print("==========================================================")
        print("HARGA TIKET $14.00")
        print(f"TOTAL HARGA SAAT INI : ${jumlahUang}")
        print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
        print("==========================================================")

    elif umur >= 65:
        jumlahUang += 18.00
        print("==========================================================")
        print("HARGA TIKET $18.00")
        print(f"TOTAL HARGA SAAT INI : ${jumlahUang}")
        print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN !!")
        print("==========================================================")

    else:
        jumlahUang += 23.00
        print("==========================================================")
        print("HARGA TIKET $23.00")
        print(f"TOTAL HARGA SAAT INI : ${jumlahUang}")
        print("TEKAN ENTER UNTUK MELANJUTKAN TRANSAKSI PEMBAYARAN!!")
        print("==========================================================")


UANGCUSTEMER = int(input("MASUKAN JUMLAH UANG ANDA : "))
TOTALKEMBALI = UANGCUSTEMER - jumlahUang
print(f"TOTAL KEMBALIAN UANG : ${TOTALKEMBALI}")
