from Animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        return super().info_animal(),
        print("Jenis Air \t\t\t : ", self.jenis_air,
              "\nBernapas \t\t\t : ", self.bernapas)
        

amphibi = Amphibi ("Katak", "Serangga", "Dua alam", "Bertelur","Air Tawar", "kulit dan pari-paru")
amphibi.info_amphibi()