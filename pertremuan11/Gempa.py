class Gempa:
    
    def __init__(self, skala, lokasi):
        self.skala = skala
        self.lokasi = lokasi

    def dampak(self):
        print(f"Ada gempa baru nich di {self.lokasi}")
        print(f"Skala dari gempa ini adalah {self.skala}")
        if self.skala < 2:
            print('Dampak ga berasa')
        elif self.skala >= 2 and self.skala <= 4:
            print('Dampak gempa bangunan retak-retak')
        elif self.skala > 4 and self.skala <= 6:
            print('Dampak gempa bangunan roboh')
        elif self.skala > 6:
            print('Dampak gempa bangunan roboh dan berpotensi tsunami')
        else :
            print('Sistem tidak dapat membaca')

    
#gempa1 = Gempa( 5.7, "Jawa barat")
#gempa1.dampak()