# Masukkan angka (bebas pakai while True)
list_angka = []

while True:
    list_angka.append(float(input("Masukkan angka: ")))
    
    if input("Ingin input lagi? (y/t): ") != "y":
        break

# Masukkan target (boleh koma)
target = float(input("\nMasukkan target: "))

# Cari pasangan
pasangan = []
jumlah_angka = len(list_angka)

for i in range(jumlah_angka):
    for j in range(i, jumlah_angka):
        if list_angka[i] + list_angka[j] == target:
            pasangan.append([list_angka[i], list_angka[j]])

# Tampilkan pasangan
print("\nPasangan yang ditemukan: ")
for i in range(len(pasangan)):
    print(f"{i + 1}. {pasangan[i][0]} + {pasangan[i][1]}")

#Tambahan opsi untuk cek terbesar, terkecil dan rata-rata
while True:
    print("\n=== Opsi Tambahan ===")
    print("1. Cek nilai terbesar")
    print("2. Cek nilai terkecil")
    print("3. Cek rata-rata")
    print("4. Keluar")

    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        print("\nNilai terbesar:", max(list_angka))

    elif pilihan == "2":
        print("\nNilai terkecil:", min(list_angka))

    elif pilihan == "3":
        rata = sum(list_angka) / len(list_angka)
        print("\nRata-rata:", rata)

    elif pilihan == "4":
        print("\nProgram selesai.")
        break

    else:
        print("\nPilihan tidak valid, coba lagi.")
