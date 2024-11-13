# Inisialisasi saldo awal dari input pengguna
saldo = int(input("Masukkan saldo awal Anda: Rp. "))

while True:
    # Tampilkan menu
    print("\nMENU ATM")
    print("1. Cek Saldo")
    print("2. Tarik Tunai")
    print("3. Setor Tunai")
    print("4. Keluar")

    # Minta input pilihan menu dari pengguna
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        # Cek Saldo
        print(f"\nSaldo Anda saat ini: Rp{saldo}")

    elif pilihan == "2":
        # Tarik Tunai
        jumlah = int(input("Masukkan jumlah yang ingin ditarik: Rp"))
        if jumlah <= saldo:
            saldo -= jumlah
            print(f"Anda telah berhasil menarik tunai Rp{jumlah}")
            print(f"Sisa saldo Anda: Rp{saldo}")
        else:
            print("Maaf, saldo Anda tidak mencukupi untuk penarikan ini.")

    elif pilihan == "3":
        # Setor Tunai
        jumlah = int(input("Masukkan jumlah yang ingin disetor: Rp"))
        saldo += jumlah
        print(f"Anda telah berhasil menyetor tunai Rp{jumlah}")
        print(f"Saldo Anda saat ini: Rp{saldo}")

    elif pilihan == "4":
        # Keluar
        print("Terima kasih telah menggunakan layanan ATM kami!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")