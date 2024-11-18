def check_nilai():
    while True:
        try:
            nilai = int(input("Masukkan nilai: "))
            if nilai < 0 or nilai > 100:
                print("Nilai tidak valid")
            elif nilai >= 90:
                print(f"Nilai {nilai} predikat A")
            elif nilai >= 80:
                print(f"Nilai {nilai} predikat B")
            elif nilai >= 70:
                print(f"Nilai {nilai} predikat C")
            elif nilai >= 60:
                print(f"Nilai {nilai} predikat D")
            else:
                print(f"Nilai {nilai} predikat E")
        except ValueError:
            print("Input tidak valid. Silakan masukkan nilai angka.")
        
        continue_check = input("Apakah Anda ingin memeriksa nilai lagi? (ya/tidak): ").strip().lower()
        if continue_check == '':
          if continue_check != 'ya': 
            print("Terima kasih! Program selesai.")
          elif continue_check != 'yo':
            print("thanks")
          elif continue_check != 'y':
            print("thanks")

check_nilai()