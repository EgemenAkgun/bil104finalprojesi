from Insan import Insan

class Issiz(Insan):
    def __init__(self, tc_no, ad, soyad, yas, cinsiyet, uyruk,tecrübe):
        super().__init__(tc_no, ad, soyad, yas, cinsiyet, uyruk)
        self.__gecmis_tecrube= tecrübe

    def get_gecmis_tecrube(self):
        return self.__gecmis_tecrube

    def set_gecmis_tecrube(self, gecmis_tecrube):
        self.__gecmis_tecrube = gecmis_tecrube
