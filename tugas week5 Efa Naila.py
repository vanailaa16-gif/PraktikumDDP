#TUGAS NO 1
kendaraan = ["honda", "mobil", "1.999cc", "merah", "4roda"]
print("list1: ")
print(kendaraan)
print()

#menambahkan harga dan tipe kendaraan dibelakang
kendaraan.append("699 juta")
kendaraan.append("sedan")

#menambahkan merek kendaraan
kendaraan.insert(2, "civic")

print("\nList kendaraan setelah ditambahkan:")
print(kendaraan)
print()

#TUGAS NO 2
print("silahkan pilih bangun datar")
print("1. persegi")
print("2. lingkaran")
print("3. segitiga")

pilih_bangun_datar = int(input("pilih bangun datar: "))

match pilih_bangun_datar:
    case 1:
        sisi = float(input("masukkan sisi: "))
        luas = sisi * sisi
        print("Luas persegi =", luas)

    case 2:
        jari_jari = float(input("masukkan jari jari: "))
        luas = 3.14 * jari_jari ** 2
        print("Luas lingkaran =", luas)

    case 3:
        alas = float(input("masukkan alas: "))
        tinggi = float(input("masukkan tinggi: "))
        luas = 0.5 * alas * tinggi
        print("Luas setiga =", luas)

    case _:
        print("kamu salah pilih")