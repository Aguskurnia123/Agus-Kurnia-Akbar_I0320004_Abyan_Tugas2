#Identitas Diri

print("Identitas Diri Sendiri")
nama = str(input("Masukan nama lengkap :"))
#umur dalam hari, bulan, tahun
tanggal_lahir = int(input("Tanggal lahir :"))
bulan_lahir = int(input("Bulan lahir (dalam angka) :" ))
tahun_lahir = int(input("Tahun lahir :"))
tanggal_ini = int(input("Masukan tanggal saat ini :"))
bulan_ini = int(input("Masukan bulan saat ini(dalam angka) :"))
tahun_ini = int(input("Masukan tahun saat ini :"))
lahir = tanggal_lahir + (bulan_lahir * 30) + (tahun_lahir * 365)
ini = tanggal_ini + (bulan_ini * 30) + (tahun_ini * 365)
umur_hari = ini-lahir
umur_bulan = (ini-lahir) /30
umur_tahun = (ini-lahir)/ 365
#alamat rumah
alamat_rumah = str(input("Desa :"))
alamat_rumah1 = str(input("Kecamatan :"))
alamat_rumah2 = str(input("Kabupaten :"))
alamat_rumah3 = str(input("Provinsi :"))
#data lain
tinggi_badan = float(input("Masukan tinggi badan :"))
ukuran_sepatu = float(input("Ukuran sepatu :"))
print("Nama Lengkap :", nama)
print("Umur :\n", "Dalam hari :", umur_hari, "\n", "Dalam bulan :", umur_bulan, "\n", "Dalam tahun :", umur_tahun)
print("Alamat :\n", "Desa :", alamat_rumah,"\n","Kecamatan :", alamat_rumah1,"\n", "Kabupaten :", alamat_rumah2, "\n", "Provinsi :", alamat_rumah3)
print("Tinggi badan(cm) :", tinggi_badan, "cm")
print("Ukuran sepatu :", ukuran_sepatu)
print("Terima Kasih :)")

