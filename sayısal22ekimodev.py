import math as mt
#Soru 1'in cevabı;
print ('Ad-Soyad: Batuhan Haybek, Numara: 1*9')
# Soru 2'nin cevabı;
a = (7 + 2**3 / (1/4) + 1 - 2 * ((3**2)*(4-2)/9))
print ("a'nin degeri: ", a)
# Soru 3'ün cevabı;
V = 20/3.6 # m/s cinsinden
phava = 1.24*9.81 # N/m**3 cinsinden
r = 20*10**(-2) # m cinsinden
A =  mt.pi * r**2 # 90 derece karşıdan bakıldığında daire çember olarak gözükecektir bu yüzden çemberin alan fomülünü kullandım
Cd = 0.25
Fd = 1/2 * Cd * phava * A * V**2 # N/m cinsinden kuvvet
print ('Fd = ',Fd, 'N/m cinsinden kuvvet')
# Soru 4'ün cevabı;
V0 = 3
teta = 30
t = 0.3
x = V0 * mt.radians(mt.cos(teta))
g = 9.81
y = V0 * mt.radians(mt.sin(teta)) * t - (1/2)*g*t**2
#print ("x ={:.2g} m, y = {:.2d} m".format(y,x))
#Soru 5' in cevabi benim yildizim TRAPPIST-1 c
i = 89.8; b = 0.11; delta = 0.0071; P = 2.421937 #  P gun cinsinden ve i derece olarak verilmis
cosi = mt.cos(i)
#Rtrappist1c = 69911 * 0.09421 # km cinsinden gezegenin yaricapi jupiterin yaricapi cinsinden olarak exoplanet.eu sitesinden aldim
#Rtrappist = 84180 # km cinsinden yildizin yaricapi
oran1 = (cosi / b)# buradaki oran1 Rtrappist/a yani yildizin yaricapi bolu yari-buyuk eksen uzunlugu olarak kullandim
print ("oran1 sonucu: ",oran1)
oran2 = mt.sqrt(delta)
print ("oran2 sonucu: ",oran2)# buradaki oran2 Rtrappist1c/Rtrappist yani gezegenin yildizin yaricapina oranini vermektedir.
Tgun = (P/mt.pi) * mt.asin(oran1 * mt.sqrt ((1 + oran2)**2 - (oran1**1 * cosi)**2)
