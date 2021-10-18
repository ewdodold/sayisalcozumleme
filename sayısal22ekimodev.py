import math as mt
#Soru 1'in cevabı;
print ('Ad-Soyad: Batuhan Haybek, Numara:16050019')
# Soru 2'nin cevabı;
a = (7 + 2**3 / (1/4) + 1 - 2 * ((3**2)*(4-2)/9))
print (a)
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
print ("x ={:.2g} m, y = {:.2d} m".format(y,x))
