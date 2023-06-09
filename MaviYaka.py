from Calisan import Calisan


class MaviYaka(Calisan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas, yipranma_payi):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas)
        self.__yipranma_payi = self.__kontrol_yipranma_payi(yipranma_payi)

    def __kontrol_yipranma_payi(self, yipranma_payi):
        try:
            if isinstance(yipranma_payi, float) and 0 <= yipranma_payi <= 1:
                return yipranma_payi
            else:
                raise ValueError("Geçersiz yıpranma payi girdisi!")
        except ValueError as e:
            print("Hata: ", e)

    def get_yipranma_payi(self):
        return self.__yipranma_payi

    def set_yipranma_payi(self, yipranma_payi):
        self.__yipranma_payi = self.__kontrol_yipranma_payi(yipranma_payi)

# zam oranını hesaplayan fonksiyon
    def zam_hakki(self):
        if self.get_tecrube() < 2:
            return self.get_yipranma_payi() * 10
        elif 2 <= self.get_tecrube() <= 4 and self.get_maas() < 15000:
            return (self.get_maas() % self.get_tecrube()) / 2 + (self.get_yipranma_payi() * 10)
        elif self.get_tecrube() > 4 and self.get_maas() < 25000:
            return (self.get_maas() % self.get_tecrube()) / 3 + (self.get_yipranma_payi() * 10)
        else:
            return self.get_maas()

    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.get_tecrube()}\nYeni Maas: {self.zam_hakki()*1/100*self.get_maas() + self.get_maas()}\n"
