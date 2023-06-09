from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,tecrübe):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__gecmis_tecrube= tecrübe

    def get_gecmis_tecrube(self):
        return self.__gecmis_tecrube

    def set_gecmis_tecrube(self, gecmis_tecrube):
        self.__gecmis_tecrube = gecmis_tecrube
#statü bulan fonksiyon
    def statu_bul(self):
        try:
            mavi_yaka_etkisi = 0.2
            beyaz_yaka_etkisi = 0.35
            yonetici_etkisi = 0.45

            max_etki = 0
            max_statu = ""

            for statu, yil in self.__gecmis_tecrube.items():
                etki = 0

                if statu == "mavi yaka":
                    etki = yil * mavi_yaka_etkisi
                elif statu == "beyaz yaka":
                    etki = yil * beyaz_yaka_etkisi
                elif statu == "yonetici":
                    etki = yil * yonetici_etkisi

                if etki > max_etki:
                    max_etki = etki
                    max_statu = statu

            return max_statu

        except Exception as e:
            print("Hata: ", e)

    def __str__(self):
        try:
            max_statu = self.statu_bul()
            return f"Ad:{self.__name},Soyad:{self.__soyad},En uygun statü: {max_statu}"

        except Exception as e:
            return f"Hata: {e}"