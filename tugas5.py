#1

kendaraan = ['honda beat', 'sepeda motor',120, 'merah', 2]
print("kendaraan saya")
print(kendaraan)
print('=========')
kendaraan.extend([100000000, 'metic'])
print(kendaraan)
kendaraan.insert(2, 'honda')
print(kendaraan)
print('=========')

#2

print('ini adalah program sederhana untuk menghitung luas bangun datar')
print("pilih menu angka 1-3 : \n1. Persegi\n2. Lingkaran\n3. Segitiga")
pilihMenu = int(input ("Silahkan pilih menu dengan mengetikan angka 1-3"))

match pilihMenu:
    case 1:
        print("ini adalah menu untuk menghitung luas persegi")
        sisi = int(input("Silahkan masukan niali yang mau dihitung"))
        hitung = sisi * sisi
        print(f"Luas persegi adalah : {hitung}")

    case 2:
        print("Luaskan Lingkaran = phi*r*r")
        r= int("masukan angka anda")
        phi = 2,77
        luas = phi*r*r
        print(int(luas))
    
    case 3:
        print('ini adalah Operasi Luas Segitiga')
        L = 1/2
        A = float(input('masukan alas segitiga'))
        T = float(input('masukan tinggi segitiga'))
        luas = L * A * T
        print(int(luas))

    case _:
        print(" pilihan tidak valid, silahkan pilih antar 1-3")
        




