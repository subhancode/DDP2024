# 1. Bilangan Genap atau Ganjil #
bilangan= int(input("masukan angka/n= "))
hasil= bilangan%2
if hasil ==0 :
    print(f"angka {bilangan} sama merupakan genap")
elif hasil ==1 :
    print(f"angka {bilangan} sama merupakan ganjil")
else:
    print("angka tidak jelas")

# 2. Nilai Ujian #
nilai= int(input("masukan nilai anda/n= "))

if nilai >=75 :
    print("kamu dinyatakan lulus")
elif nilai <75:
    print("kamu dinyatakan tidak lulus")
else :
    print("kamu tidak jelas")

if nilai >=90 :
     print(" dengan predikat A")
elif nilai >=75 :
     print(" dengan predikat B")
elif nilai >=65 :
     print(" dengan predikat c")
elif nilai <65 :
      print(" dengan predikat D")
else :
     print(" tidak tau")

# 3. Cek Usia dan Status #
usia = int(input("masukan usia anda/n= "))

if usia >=18 :
    print("kamu sudah dewasa")
elif usia >=13 and usia <=17 :
    print(" kamu saat ini sedang memasuki masa remaja")
elif usia <18 :
    print("kamu masi bocil")
else :
    print("kamu tidak di ketahui")

# 4. Cek Keanggotaan #
status =input("""silahkan pilih status 
 keanggotaan seperti dibawah ini
Gold| Silver| Bronze
masukan pilihan anda
= """)

if status.upper() == "Gold" or status.upper() == "Silver":
    print("selamat kamu mendapatkan diskon! ")
else :
    print("mohon maaf kamuu tidak mendapatkan diskon")

# 5. Pembelian Diskon #
jumlah_pembelian= int(input("masukan jumlah pembelian: "))

print(f"Anda mendapatkan diskon 10%")if jumlah_pembelian >= 100 else print("anda tidak mendapatkan diskon")
