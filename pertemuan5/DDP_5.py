#1 a
kendaraan = ['Honda Beat', 'Sepeda Motor', 120, 'Merah', 2]
print(kendaraan)

#1 b
kendaraan.append(20000000)
print(kendaraan)

#1 c
kendaraan.insert(2, 'Honda')
print(kendaraan)

#2
print('ini adalah program sederhana untuk menghitung luas bangun datar')
print(" Pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran \n3. Segitiga")
PilihMenu =int(input("Silahkan pilih menu 1-3 :"))
            
match PilihMenu :
    case 1 :
        print("Ini adalah menu untung menghitung luas persegi")
        sisi = int(input("Sisi :"))
        hitung = sisi*sisi
        print(f"Luas persegi adalah : {hitung}")
    case 2 :
        print("Ini adalah menu untung menghitung luas lingkaran")
        r = int(input("Silahkan Masukan nilai yang mau di hitung"))
        phi = 3.14
        hitung = phi*r*r
        print(f"Luas lingkaran adalah : {hitung}")
    case 3 :
        print("Ini adalah menu untung menghitung luas segitiga")
        a = int(input("alas:"))
        t = int(input("tinggi:"))
        hitung = 1/2 * a * t
        print(f"Luas segitiga adalah : {hitung}")
    case _ :
        print("Pilihan tidak valid, silahkan pilih antara 1-3")
