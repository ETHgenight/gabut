import requests

def get_weather(city_name, api_key):
    # URL API OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"

    try:
        # Mengirim permintaan HTTP GET ke API
        response = requests.get(complete_url)
        data = response.json()

        # Memeriksa apakah permintaan berhasil
        if data["cod"] != "404":
            # Mengambil data utama cuaca
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]

            # Menampilkan hasil
            print(f"Cuaca di {city_name.capitalize()}:")
            print(f"Deskripsi: {weather['description']}")
            print(f"Suhu: {main['temp']}°C")
            print(f"Suhu Minimum: {main['temp_min']}°C")
            print(f"Suhu Maksimum: {main['temp_max']}°C")
            print(f"Kelembaban: {main['humidity']}%")
            print(f"Kecepatan Angin: {wind['speed']} m/s")

        else:
            print(f"Kota {city_name} tidak ditemukan. Periksa kembali nama kotanya.")
    except Exception as e:
        print("Terjadi kesalahan:", e)

if __name__ == "__main__":
    api_key = "f5880e927082ba7a6e60201a38b60f5a"  # Ganti dengan API Key dari OpenWeatherMap
    city_name = input("Masukkan nama kota: ")
    get_weather(city_name, api_key)