import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    try:
        # Mengirim permintaan ke URL
        response = requests.get(url)
        response.raise_for_status()  # Memeriksa status respons

        # Mengurai konten HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Mengambil semua elemen judul (h1, h2, h3)
        h1_tags = soup.find_all('h1')
        h2_tags = soup.find_all('h2')
        h3_tags = soup.find_all('h3')

        print(f"\nJudul di halaman {url}:\n")
        
        # Menampilkan hasil
        for tag in h1_tags:
            print(f"H1: {tag.get_text(strip=True)}")
        for tag in h2_tags:
            print(f"H2: {tag.get_text(strip=True)}")
        for tag in h3_tags:
            print(f"H3: {tag.get_text(strip=True)}")

    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat mengakses URL: {e}")

def main():
    url = input("Masukkan URL halaman web yang ingin di-scrape: ")
    scrape_titles(url)

if __name__ == "__main__":
    main()
