# #READ LIST

# #A
# namaBuah = ["jeruk","mangga","semangka","mangga"]
# print(namaBuah)

# #B
# namaBuah = ["jeruk","mangga","semangka","mangga"]
# print(namaBuah[1])

# #C
# namaBuah = ["jeruk", "mangga", "semangka", "mangga"]
# print(namaBuah[0:2])

# #INSERT LIST

# #A
# namaBuah = ["jeruk", "mangga", "semangka", "mangga"]
# print(namaBuah)
# namaBuah.append("anggur")
# namaBuah.insert(4, "leci")
# print(namaBuah)

#* C
# namaBuah = ["jeruk", "mangga", "semangka", "mangga"]
# namaSayur = ["wortel", "tomat"]
# print(f"ini nama buah (namaBuah)")
# print(f"ini nama sayur (namaSayur)")
# namaBuah.extend(namaSayur)
# print(f"ini nama buah setelah perubahan (namaBuah)")
# print(f"ini nama sayur setelah perubahan (namaSayur)")

#* UPDATE LIST

# namabuah = ["jeruk", "mangga", "semangka", "mangga"] 
# print (f"Daftar buah lama = {namaBuah}")
# namaBuah [3] = "kelengkeng"
# print (f"Daftar buah baru = {namaBuah}")

# namaBuah = ["jeruk", "mangga", "semangka", "mangga"]
# print(f"Daftar buah lama = {namaBuah}")
# namaBuah [1:3] = ["kelengkeng","anggur"]
# print(f"Daftar buah lama = {namaBuah}")

#* DELETE LIST 

# namaBuah = ["Jeruk", "mangga", "semangka", "mangga"]
# namaBuah.remove("mangga")
# print(namaBuah)

# namaBuah = ["jeruk", "mangga", "semangka", "mangga"] 
# namaBuah.pop(1) 
# print(namaBuah)

# namaBuah = ["Jeruk", "mangga", "semangka", "mangga"] 
# namaBuah.pop() 
# print(namaBuah)

# namaBuah = ["Jeruk", "mangga", "semangka", "mangga"]
# del namaBuah [0]
# print(namaBuah)

# namaBuah = ["jeruk", "mangga", "semangka", "mangga"] 
# del namaBuah 
# print(namaBuah)

# namaBuah = ["Jeruk", "mangga", "semangka", "mangga"]
# namaBuah.clear()
# print(namaBuah)

nilai = [78, 80, 90, 85, 80] # Mengubah kurung yang awalnya '<>' menjadi '[]'
totalNilai = 0
counter = 1

for nilai in nilai:
    counter += 1
    print(f"nilai ke {counter} = {totalNilai}")
    totalNilai += nilai

rerataNilai = totalNilai / len(totalNilai) # Mengubah variabel nilai menjadi totalNilai
print(f"hasil rata-rata nilai seluruh siswa adalah {rerataNilai}")

hargaProduk = [32000,13000,15000, 11000]
namaProduk = ["Sunco", "So Klin", "Sun Light", "Mie Telor"]
counter = 0
index = 0
totalBelanja = 0
selectedProducts = []

totalBelanja = 0
selectedProducts = []


print("SELAMAT DATANG DI TOKO MAKMUR JAYA")
print("DAFTAR PRODUK HARI INI :")

for np in namaProduk:
    counter += 1
    print(f"{counter}, {np} - Rp. {hargaProduk[counter-1]} ")
    index += 1

print("5. Selesai belanja")
print("6. Gak jadi belanja deh")
print("7. Hapus produk yang dipilih")


while True:
    pilihan = int(input("Mau belanja apa hari ini (1/2/3/4/5/6/7)? "))

    if pilihan == 1:
        totalBelanja += hargaProduk[0]
        selectedProducts.append((namaProduk[0], hargaProduk[0]))

    elif pilihan == 2:
        totalBelanja += hargaProduk[1]
        selectedProducts.append((namaProduk[1], hargaProduk[1]))

    elif pilihan == 3:
        totalBelanja += hargaProduk[2]
        selectedProducts.append((namaProduk[2], hargaProduk[2]))

    elif pilihan == 4:
        totalBelanja += hargaProduk[3]
        selectedProducts.append((namaProduk[3], hargaProduk[3]))


    elif pilihan == 5:
        print("------------------------------------------------")
        print(f"Total Belanja anda adalah Rp. {totalBelanja}\n")
        print("TERIMA KASIH SUDAH BERBELANJA")
        break

    elif pilihan == 6:
        print("------------------------------------------------")
        print("Anda tidak jadi berberlanja")
        break

    elif pilihan == 7:
        if not selectedProducts:
            print("Belum ada produk yang dipilih.")
        else:
            print("Produk yang dipilih:")
            for i in range(len(selectedProducts)):
                product = selectedProducts[i]
                print(f"{i+1}. {product[0]} - Rp. {product[1]}")
            choice = int(input("Masukkan nomor produk yang ingin dihapus: ")) - 1

            if 0 <= choice < len(selectedProducts):
                totalBelanja -= selectedProducts[choice][1]
                del selectedProducts[choice]
                print("Produk berhasil dihapus.")
            else:
                print("Nomor tidak valid.")

    else:
        print("Mohon maaf pilihan tidak tersedia")


# antrian = [] 
# pemeriksaan = []
# rekap_hari_ini = []

# while True: 
#     print("\n=== Sistem Informasi Rumah Sakit ===") 
#     print("1. Tambah Antrian") 
#     print("2. Panggil Pasien") 
#     print("3. Input Hasil Pemeriksaan") 
#     print("4. Tampilkan Rekap Hari Ini") 
#     print("5. Keluar") 
#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         nama = input("Masukkan nama pasien: ")
#         antrian.append(nama)
#         rekap_hari_ini.append(nama)
#         print(f"{nama} telah ditambahkan ke dalam antrian.")

#     elif pilihan == "2":
#         if antrian:
#             pasien = antrian.pop(0)
#             pemeriksaan.append(pasien)
#             print(f"Memanggil pasien: {pasien}")
#         else:
#             print("Tidak ada pasien dalam antrian.")

#     elif pilihan == "3":
#         if pemeriksaan:
#             pasien = pemeriksaan.pop(0)
#             status = input(f"{pasien} termasuk (Rawat Jalan/Rawat Inap): ")
#             biaya = input("Masukkan biaya pemeriksaan: ")
#             print(f"Hasil: {pasien} - {status} - Biaya: {biaya}")
#         else:
#             print("Tidak ada pasien dalam pemeriksaan.")

#     elif pilihan == "4":
#         print("\nRekap Pasien Hari Ini:")
#         for pasien in rekap_hari_ini:
#             print(f"- {pasien}")
#         print("\nAntrian Saat Ini:")
#         for pasien in antrian:
