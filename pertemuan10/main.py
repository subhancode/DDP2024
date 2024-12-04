import math 

def l_segitiga(alas, tinggi):
    luassgt = 1/2 * alas * tinggi 
    print(f'Luas Segitiga {1/2} * {alas} * {tinggi} = {luassgt}')

def l_persegi(sisi):
    luas = sisi * sisi
    keliling = sisi*sisi*sisi*sisi
    print(f'Luas persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling persegi adalah {keliling}')

def l_persegipanjang(panjang, lebar):
    luaspsgpnjg = panjang * lebar
    print(f'Luas persegi panjang {panjang} * {lebar} = {luaspsgpnjg}')

def l_lingkaran(jari_jari):
    luas = math.pi * jari_jari ** 2
    print(f"Luas lingkaran dengan jari-jari {jari_jari} = {luas:.2f}")

def l_jajargenjang(alas, tinggi):
    luas = alas * tinggi
    print(f"Luas jajar genjang dengan alas {alas} dan tinggi {tinggi} = {luas}")

def l_balok(panjang, lebar, tinggi):
    luasbalok = 2 * (panjang*lebar) + (panjang*tinggi) + (lebar*tinggi)
    print(f'Luas balok adalah {luasbalok}')

def l_kubus(sisi):
    luaskubus = 6 * (sisi*sisi)
    print(f'Luas Kubus adalah {luaskubus}')

def l_tabung(jari2, tinggi):
    luastabung = 2 * 22/7 * (jari2 + tinggi)
    print(f'Luas Tabung adalah {luastabung}')

def l_limassegiempat(sisi, sisitegak):
    luaslimassgempt = (sisi*sisi) + (4*sisitegak)
    print(f'Luas Limas Segiempat adalah {luaslimassgempt}')
    
def l_prismasegitiga(luasalas, sisitegak):
    luasprismasgt = (2*luasalas) + (3*sisitegak)
    print(f'Luas Prisma Segitiga Adalah {luasprismasgt}')