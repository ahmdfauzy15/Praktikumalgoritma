def write(string):
    file = open("tes.txt","w")
    file.write(str(string))
    file.close()
    
def read ():
    file = open("tes.txt", "r")
    teks = file.read()
    print(teks)
    
nama = str(input("Nama:"))
umur = str(input("Umur:"))
alamat = str(input("Alamat:"))
email = str(input("email:"))
dosen = str(input("nama dosen:"))
teks = ("Nama: {}\nUmur: {}\nAlamat: {}\nemail: {}\ndosen: {}").format(nama, umur, alamat,email,dosen)

write(teks)
read()
