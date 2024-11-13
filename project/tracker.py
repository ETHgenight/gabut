import requests

def track_location(ip_address, api_key=None):
    # Jika ada API key, gunakan; jika tidak, gunakan URL tanpa API key
    if api_key:
        url = f"https://ipinfo.io/{ip_address}?token={api_key}"
    else:
        url = f"https://ipinfo.io/{ip_address}"

    try:
        response = requests.get(url)
        data = response.json()

        # Menampilkan informasi lokasi
        if "bogon" not in data:
            print(f"IP Address: {data.get('ip', 'Tidak tersedia')}")
            print(f"Lokasi: {data.get('city', 'Tidak tersedia')}, {data.get('region', 'Tidak tersedia')}, {data.get('country', 'Tidak tersedia')}")
            print(f"Organisasi: {data.get('org', 'Tidak tersedia')}")
            print(f"Kode Pos: {data.get('postal', 'Tidak tersedia')}")
            print(f"Koordinat: {data.get('loc', 'Tidak tersedia')}")
        else:
            print("IP ini adalah IP privat (bogon), dan tidak memiliki data lokasi.")
    except Exception as e:
        print(f"Terjadi kesalahan saat mengakses API: {e}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Masukkan API Key dari ipinfo.io atau kosongkan jika tidak ada
    ip_address = input("Masukkan alamat IP yang ingin dilacak (atau kosongkan untuk IP publik Anda): ")
    
    # Jika ip_address kosong, gunakan 'me' untuk mendapatkan info IP publik sendiri
    if not ip_address:
        ip_address = "me"
    
    track_location(ip_address, api_key)