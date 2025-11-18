# Pastikan jumlah angka 5 - 10
jumlah_angka = 0
while jumlah_angka > 10 or jumlah_angka < 5:
    jumlah_angka = int(input("Masukkan jumlah angka(5-10): "))

# Masukkan angka
list_angka = []
for i in range(jumlah_angka):
    list_angka.append(int(input(f"Masukkan angka ke {i + 1}: ")))

# Masukkan target
target = int(input("\nMasukkan target: "))

# Cari pasangan
pasangan = []
for i in range(jumlah_angka):
    for j in range(i, jumlah_angka):
        if list_angka[i] + list_angka[j] == target:
            pasangan.append([list_angka[i], list_angka[j]])

# Tampilkan pasangan
print("\nPasangan yang ditemukan: ")
for i in range(len(pasangan)):
    print(f"{i + 1}. {pasangan[i][0]} + {pasangan[i][1]}")