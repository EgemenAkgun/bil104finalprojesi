from Insan import Insan

class Calisan(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk, sektor, tecrube, maas):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__sektor = self.__kontrol_sektor(sektor)
        self.__tecrube = tecrube
        self.__maas = maas

    def __kontrol_sektor(self, sektor):
        try:
            sektorler = ["teknoloji", "muhasebe", "inşaat", "diğer"]
            if sektor.lower() in sektorler:
                return sektor.lower()
            else:
                raise ValueError("Geçersiz sektor girdisi!")
        except ValueError as e:
            print("Hata: ", e)

    def get_sektor(self):
        return self.__sektor

    def set_sektor(self, sektor):
        self.__sektor = self.__kontrol_sektor(sektor)

    def get_tecrube(self):
        return self.__tecrube

    def set_tecrube(self, tecrube):
        self.__tecrube = tecrube

    def get_maas(self):
        return self.__maas

    def set_maas(self, maas):
        self.__maas = maas
#zam oranını hesaplayan fonksiyon
    def zam_hakki(self):
        if self.__tecrube < 2:
            return 0
        elif self.__tecrube >= 2 and self.__tecrube <= 4 and self.__maas < 15000:
            return self.__maas % self.__tecrube
        elif self.__tecrube > 4 and self.__maas < 25000:
            return (self.__maas % self.__tecrube) / 2
        else:
            return self.__maas
#zam oranı olduğu için  zam hakki*1/100 * maas + maas yaptım
    def __str__(self):
        return f"Ad: {self.get_ad()}\nSoyad: {self.get_soyad()}\nTecrube: {self.__tecrube}\nYeni Maas: {self.zam_hakki()*1/100*self.get_maas() + self.get_maas()}\n"
