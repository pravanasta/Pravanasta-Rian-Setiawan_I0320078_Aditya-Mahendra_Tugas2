import math

#Menampilkan judul
print("============================================")
print("   Menghitung Luas dan Keliling Lingkaran   ")
print("============================================")

#Input jari-jari lingkaran
r = float(input("Masukkan nilai jari-jari :"))

#Menghitung luas dan keliling lingaran
luas = 3.14 * r ** 2
keliling = 3.14 * 2 * r

#Menampilkan informasi
print("\nLuas lingkaran anda adalah :", luas)
print("Keliling lingkaran anda adalah :", keliling)

print("============================================")
print("   Selesai  ")
print("============================================")