print("======================================")
print("   Biodata Saya  ")
print("======================================")

#Biodata Pribadi
namaDepan = "Pravanasta"
namaTengah = "Rian"
namaBelakang = "Setiawan"
nama = namaDepan + " " + namaTengah + " " + namaBelakang
nim = "I0320078"
jurusan = "Teknik industri"
angkatan = 2020
tinggi = 180
alamat = "Krajan, koripan, Matesih, Karanganyar, Jawa Tengah"

#Informasi Tanggal lahir
Tanggal_sekarang = 13
Bulan_sekarang = 3
Tahun_sekarang = 2021
Tanggal_lahir = 2
Bulan_lahir = 11
Tahun_lahir = 2001

lahir = Tanggal_lahir+(Bulan_lahir*30)+(Tahun_lahir*365)
aktual = Tanggal_sekarang+(Bulan_sekarang*30)+(Tahun_sekarang*365)

#memulai proses kalkulasi
tahun = int((aktual-lahir)/365)
bulan = float(((aktual-lahir)%365)/30)
hari = ((aktual-lahir)%365)%30

#Hasil
print("Nama saya", nama)
print("Nim saya", nim)
print("Saya kuliah di jurusan", jurusan)
print("Saya merupakan mahasiswa angkatan", angkatan)
print("Saya memiliki tinggi badan", tinggi)
print("Saya tinggal di", alamat)
print("Saya berumur: ")
print(hari, "hari")
print(bulan, "bulan")
print(tahun, "tahun")

print("======================================")
print("   Terima Kasih  ")
print("======================================")
