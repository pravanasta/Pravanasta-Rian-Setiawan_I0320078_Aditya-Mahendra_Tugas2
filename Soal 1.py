##Menghitung Luas Persegi Panjang
#menampilkan informasi program
print("MENGHITUNG LUAS PERSEGI PANJANG")

#input nilai panjang dan lebar
panjang = float(input("Masukan Panjang: "))
lebar = float(input("Masukan Lebar: "))

#menghitung luas persegi panjang
luas = panjang*lebar

#menampilkan hasil perhitungan
print("Luas Persegi Panjang: ",luas)


##Menghitung Luas Lingkaran
#menampilkan informasi program
print("MENGHITUNG LUAS LINGKARAN")

phi = 3.14

#input nilai jari-jari
r = float(input("Masukkan jari-jari lingkaran: "))

#menghitung luas lingkaran
Luas_Lingkaran = phi*r*r

#menampilkan hasil perhitungan
print("Luas Lingkaran: ",Luas_Lingkaran)


##Menghitung Luas Permukaan Kubus
#menampilkan informasi program
print("MENGHITUNG LUAS PERMUKAAN KUBUS")

#input nilai sisi
sisi = float(input("Masukan sisi kubus: "))

#menghitung luas permukaan kubus
Luas_Permukaan = 6*(sisi*sisi)

#menampilkan hasil perhitungan luas
print("Luas Permukaan Kubus: ",Luas_Permukaan)


##Menghitung Konversi Suhu Celcius Ke Fahrenheit
#menampilkan informasi program
print("MENGHITUNG KONVERSI SUHU CELCIUS KE FAHRENHEIT")

#input suhu dalam celcius
suhu = float(input("Masukan Suhu dalam Celcius: "))

#mengkonversi suhu dalam celcius ke fahrenheit
suhu_fahrenheit = (suhu*9/5)+32

#menampilkan hasil perhitungan
print("Suhu dalam Fahrenheit: ",suhu_fahrenheit )


##Menghitung Konversi Suhu Reamur Ke Kelvin
#menampilkan informasi program
print("MENGHITUNG KONVERSI SUHU REAMUR KE KELVIN")

#input suhu dalam reamur
suhu = float(input("Masukan Suhu dalam Reamur: "))

#mengkonversi suhu dalam reamur ke kelvin
suhu_kelvin = (suhu*5/4)+273

#menampilkan hasil perhitungan
print("Suhu dalam kelvin: ",suhu_kelvin )
