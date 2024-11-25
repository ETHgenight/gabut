# == sama dengan
# > lebih dari
# < kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <= kurang dari sama dengan


#  TUGASS TAXI ONLINE
# variabel taxi online     
#waktu_perjalanan = int(input("Masukkan waktu perjalanan: "))
#jarak_tempuh = int(input("Masukkan jarak tempuh: "))
#tarif = 15000

    #tarif dasar taxi online
#if waktu_perjalanan < 30 and jarak_tempuh < 10:
    #tarif = 15000

#elif waktu_perjalanan >= 30 or jarak_tempuh >= 10:
    #tarif = 20000
    #tambahan biaya jika menambah 10 kmt
    #if jarak_tempuh > 10:
        #tambahan_km = jarak_tempuh - 10
        #tarif += tambahan_km * 2000
    #hasil dari outputnya
    #print(f"Tarif perjalanan Anda adalah: Rp {tarif}")

#   TUGAS SENTIMEN oktober-7-SENIN
#produk_yang_dibeli = input("produk apa yang baru kamu beli? ")
#komentar_produk_yang_dibeli = input(f"Apa komentar mu tentang produk {produk_yang_dibeli} yang baru kamu beli ? ")

#def analisa_komentar(komentar):
#    hasil = []
#    for komen in komentar.split(" "):
#        if "buruk" in komen and not "buruk" in hasil:
#            hasil.append("buruk")
#        elif "baik" in komen and not "baik" in hasil:
#            hasil.append("baik")


#    if len(hasil) == 1 and "baik" in hasil:
#        return "1baik"
#    elif len(hasil) == 1 and "buruk" in hasil:
#        return "1buruk"
#    elif len(hasil) == 2 and (("baik" in hasil) and ("buruk" in hasil)):
#        return "baik, buruk"
#    else:
#        return "invalid"


#hasil_analisa_komentar = analisa_komentar(komentar_produk_yang_dibeli)
#if "1baik" in hasil_analisa_komentar:
#    print("Anda mengomentari produk ini baik.")
#elif "1buruk" in hasil_analisa_komentar:
#    print("Anda mengomentari produk ini buruk.")
#elif "baik, buruk" in hasil_analisa_komentar:
#    print("Anda mengomentari produk ini netral")
#else:
#    print("Kamu tidak masuk kualifikasi analisa sentimen (baik/buruk) kami.")


# for x in range(1,10):
#     print(x)

# for x in "soto":
#     print(x)

# namaBuah = ["apel","jeruk","semangka"]
# for buah in namaBuah: 
#     print(buah)#

# nilai = 3 
# while nilai <= 9:
#     print (f"{nilai} - ""hello")
#     nilai += 3



# jumlahKata = 0 #inisialisasi
# kalimat = input("Masukkan kalimatmu.. : ") 
# kata = kalimat.split() #memisah setiap kata, contoh = ["apa ka     barmu"]  menjadi ["apa", "kabarmu"]

# for tiapkata in kata: 
#     jumlahKata += 1 
#     print(f"{tiapkata} adalah kata ke {jumlahKata}")

# print(f"jumlah kata {jumlahKata}")


import random #untuk memasukkan module angka acak
angka_rahasia = random.randint(1, 100) #angka acak antara 1-100
tebakan = 0
percobaan = 0
print("Hai, ayo kita bermain tebak angka!")
print("Saya telah memilih angka antara 1 sampai 100.")
while tebakan != angka_rahasia:
    try:                                        #try dan except untuk mengubah inisialisasi / suatu nilai 
                                                #sehingga kondisi tidak terpenuhi / perulangan berhenti
        tebakan = int(input("Tebakan Anda: "))
        percobaan += 1

        if tebakan < angka_rahasia:
            print("Terlalu rendah. Coba lagi!")

        elif tebakan > angka_rahasia:
            print("Terlalu tinggi. Coba lagi!")

    except ValueError:                          #program menampilkan "masukkan angka yang valid" ketika input bukan angka
        print("Masukkan angka yang valid!")

print(f"Selamat! Anda berhasil menebak dalam {percobaan} percobaan.") 

# a = input("masukkan angka pertama : ")
# b = input("masukkan angka kedua : ") 

