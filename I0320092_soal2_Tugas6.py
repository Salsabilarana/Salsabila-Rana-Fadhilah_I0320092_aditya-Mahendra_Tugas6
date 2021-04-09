#menghitung rata-rata nilai

nilai = (input("Masukan list nilai, pisahkan dengan koma:"))
list = nilai.split(",")
nilai_baru = [int(x) for x in list]

jumlah = 0
for angka in nilai_baru:
    jumlah += angka
    rata_rata= jumlah / len(nilai_baru)

print("Nilai rata-rata :", rata_rata)

