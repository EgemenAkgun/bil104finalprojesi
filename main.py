import pandas as pd
from Insan import Insan
from Issiz import Issiz
from Calisan import Calisan
from MaviYaka import MaviYaka
from BeyazYaka import BeyazYaka

# İnsan sınıfı için 2 nesne oluşturulması ve bilgilerin yazdırılması
insan1 = Insan("11111111111", "Ahmet", "Demir", 35, "Erkek", "Türk")
insan2 = Insan("66666666666", "Ayşe", "Kara", 28, "Kadın", "Türk")
print(insan1)
print(insan2)

# İşsiz sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
issiz1 = Issiz("11111111111", "Ahmet", "Demir", 35, "Erkek", "Türk", "Üniversite mezunu")
issiz2 = Issiz("22222222222", "Mehmet", "Yılmaz", 40, "Erkek", "Türk", "Lise mezunu")
issiz3 = Issiz("33333333333", "Ayşe", "Yıldız", 28, "Kadın", "Türk", "Ortaokul mezunu")
print(issiz1)
print(issiz2)
print(issiz3)

# Çalışan sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
calisan1 = Calisan("44444444444", "Ahmet", "Kaya", 30, "Erkek", "Türk", "Teknoloji", 3, 12000)
calisan2 = Calisan("55555555555", "Mehmet", "Yılmaz", 35, "Erkek", "Türk", "Muhasebe", 5, 18000)
calisan3 = Calisan("66666666666", "Ayşe", "Kara", 28, "Kadın", "Türk", "İnşaat", 2, 10000)
print(calisan1)
print(calisan2)
print(calisan3)

# Mavi Yaka sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
mavi_yaka1 = MaviYaka("77777777777", "Ahmet", "Demir", 32, "Erkek", "Türk","İnşaat", 1, 14000,0.2)
mavi_yaka2 = MaviYaka("88888888888", "Mehmet", "Yılmaz", 37, "Erkek", "Türk","Muhasebe",3 , 20000,0.5)
mavi_yaka3 = MaviYaka("99999999999", "Ayşe", "Yıldız", 29, "Kadın", "Türk","Teknoloji",5 , 12000,0.3)
print(mavi_yaka1)
print(mavi_yaka2)
print(mavi_yaka3)

# Beyaz Yaka sınıfı için 3 nesne oluşturulması ve bilgilerin yazdırılması
beyaz_yaka1 = BeyazYaka("10101010101", "Ahmet", "Kaya", 30, "Erkek", "Türk", "Teknoloji", 3, 12000, 500)
beyaz_yaka2 = BeyazYaka("12121212121", "Mehmet", "Yılmaz", 35, "Erkek", "Türk", "Muhasebe", 5, 18000, 2500)
beyaz_yaka3 = BeyazYaka("13131313131", "Ayşe", "Kara", 28, "Kadın", "Türk", "İnşaat", 2, 10000, 1000)
print(beyaz_yaka1)
print(beyaz_yaka2)
print(beyaz_yaka3)

# Çalışan, mavi yaka ve beyaz yaka nesnelerinden bir DataFrame oluşturulması
