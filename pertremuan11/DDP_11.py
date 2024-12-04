# pendeklarasian class
class orang:
    #variabel(atribut)
    nama =""
    umur = 0

    #fungsi(method)
    def ngomong(self):
        print("Halo, saya adalah orang")

# membuat objek
supir = orang()
supir.nama = "Budi"
supir.umur = 30
print(supir.nama)
print(supir.umur)
supir.ngomong()

dokter = orang()
dokter.sertifikat = "1234567"
print(dokter.nama)
print(dokter.sertifikat)

mahasiswa = orang()
mahasiswa.nim = "211283732"
mahasiswa.prodi = "Teknik Informatika"
print(mahasiswa.nama)
print(mahasiswa.nim)
print(mahasiswa.prodi)

class mobil:
    bensin = ""
    merek = ""
    
    def maju(self):
        print("Mobil Berjalan")

kijang = mobil()
kijang.maju