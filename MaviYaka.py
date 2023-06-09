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

