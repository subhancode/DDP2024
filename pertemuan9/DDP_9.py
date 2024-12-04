# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
print('## Nomor 1 ##')
def celcius_ke_fahrenheit(celcius):
    fahrenheit=(celcius*9/5)+32
    return fahrenheit

suhu_celcius1 = 0
suhu_celcius2 = 100 
#cetak 0 celcius ke 32 fahrenheit
suhu_fahrenheit1 =celcius_ke_fahrenheit(suhu_celcius1)
print('Suhu Celcius', suhu_celcius1, 'sama dengan', suhu_fahrenheit1)
#cetak 100 celcius ke 212 fahrenheit
suhu_fahrenheit2 =celcius_ke_fahrenheit(suhu_celcius2)
print('Suhu Celcius', suhu_celcius2, 'sama dengan', suhu_fahrenheit2)

#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
print()
print('## Nomor 2 ##')
def genap_ganjil(bilangan):
    hitung = bilangan % 2 == 0
    return hitung

angka = 4
hasil = genap_ganjil(angka)
print (f"Bilangan {angka} bernilai {hasil}")

angka2 = 7
hasil2 = genap_ganjil(angka2)
print (f"Bilangan {angka2} bernilai {hasil2}")

#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
print()
print('## Nomor 3 ##')
def cek_kelulusan(nilai):
    if nilai >60:
        return 'Lulus'
    else:
        return 'Gagal'
    
nilai_kamu = 80
status = cek_kelulusan(nilai_kamu)
print(f"nilai: {nilai_kamu}, status: {status}")

nilai_kamu = 60
status = cek_kelulusan(nilai_kamu)
print(f"nilai: {nilai_kamu}, status: {status}")

#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
print()
print('## Nomor 3 ##')

def cek_ganjil(bilangan):
    for i in range(1, bilangan):
        if i % 2 != 0:
            print(i, end=", ")
    print(bilangan-1)  #untuk mencetak angka ganjil terakhir

cek_ganjil(20) 

