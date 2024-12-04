#no 1
kendaraan = input ("Masukan kendaraan yang dipakai? (motor,mobil) : ")
bensin = input ("Masukan bensin yang dipakai? (Pertamax, Pertalite, Pertamax Turbo) ")

if bensin == "pertalite" :
    harga = 10000
    jarak_tempuh = 12
elif bensin == "pertamax" :
    harga = 14000
    jarak_tempuh = 13
elif bensin == "pertamax turbo" :
    harga = 17000
    jarak_tempuh = 13.5


kota = input ("masukan kota ? ")

if kota == "jakarta" :
    jarak = 20
elif kota == "bekasi" :
    jarak = 15
elif kota == "depok":
    jarak = 5
elif kota == "tanggerang":
    jarak = 99
elif kota == "bogor":
    jarak = 120.6
    
    
pemakaian_bensin = jarak / jarak_tempuh
total_harga = pemakaian_bensin * harga 



print(f"Kendaraan: {kendaraan}")
print(f"Jenis Bensin: {bensin}")
print(f"Kota yang Dituju: {kota}")
print(f"Jarak ke Kota Tujuan: {jarak} KM")
print(f"Pemakaian Bensin: {pemakaian_bensin:.2f} liter")
print(f"Total Harga Bensin: Rp {total_harga:.2f} ")


#no 2
menu_makanan = {
    "Nasi Goreng": 15000,
    "Mie Goreng": 12000,
    "Ayam Geprek": 18000
}

menu_minuman = {
    "Aneka Jus": 15000,
    "Soft Drink": 10000,
    "Sweet Ice Tea": 5000
}

pembeli = input ("Masukan nama pembeli : ")
no_hp = input ("Masukan nomor telepon : ")

menu_pesanan = input ("Masukan pesanan kamu Makanan atau Minuman : ")

if menu_pesanan == "Makanan":
    print ("\n Menu Makanan :")
    for item, harga in menu_makanan.items():
        print (f"{item} - Rp {harga}")
        
elif menu_pesanan == "Minuman":
    print ("\n Menu Minuman :")
    for item, harga in menu_minuman.items():
        print (f"{item} - Rp {harga}")
        
else: 
    print ("Menu yang kamu pilih tidak ada")

menu = input ("\n Masukan Menu yang kamu mau : ")
jumlah = int(input ("Masukan jumlah pesanan : "))

if menu_pesanan == "Makanan" and menu in menu_makanan:
    hargasatuan = menu_makanan[menu]
elif menu_pesanan == "Minuman" and menu in menu_minuman:
    hargasatuan = menu_minuman[menu]
else:
    print ("Menu yang kamu pilih tidak ada")
    
total = hargasatuan * jumlah

print (f"Nama Pembeli : {pembeli} ")
print (f"No HP : {no_hp} ")
print (f"Menu yang dipesan : {menu} ")
print (f"Jumlah pesanan : {jumlah} ")
print (f"Jadi total yang harus dibayar adalah : Rp {total}")


#no 3 
for i in range(1, 21):
    if i % 3 == 0:
        print("STT Nurul Fikri")
    else:
        print(i)

