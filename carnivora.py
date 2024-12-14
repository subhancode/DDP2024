from Animal import Animal

# setiap class child itu memiliki 2 properti dan method
class Carnivora1(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, tipe_hewan, cara_berburu, ciri ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.tipe_hewan = tipe_hewan
        self.cara_berburu = cara_berburu
        self.ciri = ciri

    def info_carnivora1(self):
        super().info_animal()
        print("tipe hewan \t\t\t : ", self.tipe_hewan,
        "\ncara berburu \t\t\t :", self.cara_berburu,
        "\nciri \t\t\t\t :", self.ciri,
        '\n---------------------------------------'
        )

Carnivora1 = Carnivora1("elang", "ikan, ayam, tikus", "udara", "vivipar", "burung pemangsa", "Terbang tinggi dan menyambar mangsa", "penglihatannya tajam")
Carnivora1.info_carnivora1()

# class 2
class Carnivora2(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, tipe_hewan, cara_berburu, ciri ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.tipe_hewan = tipe_hewan
        self.cara_berburu = cara_berburu
        self.ciri = ciri

    def info_carnivora2(self):
        super().info_animal()
        print("tipe hewan \t\t\t : ", self.tipe_hewan,
        "\ncara berburu \t\t\t :", self.cara_berburu,
        "\nciri \t\t\t\t :", self.ciri,
        '\n---------------------------------------'
        )

Carnivora2 = Carnivora2("serigala", "hewan ternak, bangkai", "darat", "vivipar", "mamalia predator dari keluarga anjing", "berburu mangsa secara tim", "hidup berkelompok")
Carnivora2.info_carnivora2()

# class 3
class Carnivora3(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, tipe_hewan, cara_berburu, ciri ):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.tipe_hewan = tipe_hewan
        self.cara_berburu = cara_berburu
        self.ciri = ciri

    def info_carnivora3(self):
        super().info_animal()
        print("tipe hewan \t\t\t : ", self.tipe_hewan,
        "\ncara berburu \t\t\t :", self.cara_berburu,
        "\nciri \t\t\t\t :", self.ciri,
        '\n---------------------------------------'
        )
        
Carnivora3 = Carnivora3("macan", "daging", "hutan tropis, padang rumput", "vivipar", "kucing besar", "memanjat pohon, mengintai mangsanya", "memiliki pola totol totol hitam")
Carnivora3.info_carnivora3()