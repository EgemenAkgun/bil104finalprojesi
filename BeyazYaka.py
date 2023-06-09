from Calisan import Calisan


class BeyazYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, tesvik_primi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__tesvik_primi = self.__kontrol_tesvik_primi(tesvik_primi)

    def __kontrol_tesvik_primi(self, tesvik_primi):
        try:
            if isinstance(tesvik_primi, (int, float)) and tesvik_primi >= 0:
                return tesvik_primi
            else:
                raise ValueError("Geçersiz teşvik primi girdisi!")
        except ValueError as e:
            print("Hata: ", e)

    def get_tesvik_primi(self):
        return self.__tesvik_primi

    def set_tesvik_primi(self, tesvik_primi):
        self.__tesvik_primi = self.__kontrol_tesvik_primi(tesvik_primi)

# zam miktarını hesaplayan fonksiyon
    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.get_tesvik_primi()
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() % self.get_tecrube()) * 5 + self.get_tesvik_primi()
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() % self.get_tecrube()) * 4 + self.get_tesvik_primi()
        else:
            return self.get_maas()

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()}\nYeni Maas: {self.zam_hakki() + self.get_maas()}\n"
