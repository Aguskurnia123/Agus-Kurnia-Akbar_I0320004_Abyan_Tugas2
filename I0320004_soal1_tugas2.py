import math

#menghitung luas persegi panjang
print("Luas Persegi Panjang")
p = float(input("Masukan panjang : "))
l = float(input("Masukan lebar : "))

L = p*l

print("Luas Persegi Panjang = ", L )
print("      ")

#menghitung luas lingkaran
print("Luas Lingkaran")
r = float(input("Masukan jari-jari : "))

L = 3.14 * (r**2)

print("Luas Lingkaran : ", L)
print("      ")

#menghitung luas kubus
print("Menghitung Luas Kubus")
s = float(input("Masukan rusuk :"))

luas_kubus = (s**2)*6
print("Luas Kubus : ", luas_kubus)
print("      ")

#konversi suhu celcius ke fahrenheit
print("Konversi Suhu (Celcius ke Fahrenheit)")
c= float(input("Masukan Suhu (dalam Celcius): "))
F= (c*(9/5)) + 32
print("Suhu dalam Celcius :", c)
print("Suhu dalam Fahrenheit :", F)
print("          ")

#konversi suhu reamur ke kelvin
print("Konversi Suhu (Reamur ke Kelvin)")
r= float(input("Masukan Suhu (dalam Reamur) :"))
K=(((5/4)*r)+273)
print("Suhu dalam Reamur :", r)
print("Suhu dalam Kelvin :", K)

