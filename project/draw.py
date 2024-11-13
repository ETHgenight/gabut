import cv2
import mediapipe as mp
import numpy as np

# Inisialisasi Mediapipe dan variabel global
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Warna default dan canvas
warna = (0, 0, 255)  # Merah
canvas = None
is_erasing = False

# Fungsi untuk memilih warna
def pilih_warna(x, y):
    global warna
    if 0 < x < 50 and 0 < y < 50:
        warna = (0, 0, 255)  # Merah
    elif 50 < x < 100 and 0 < y < 50:
        warna = (0, 255, 0)  # Hijau
    elif 100 < x < 150 and 0 < y < 50:
        warna = (255, 0, 0)  # Biru

# Fungsi untuk menggambar dengan jari telunjuk
def gambar_tangan(landmark1, landmark2):
    global canvas
    cv2.line(canvas, landmark1, landmark2, warna, 5)

# Fungsi untuk reset gambar
def reset_gambar(frame):
    global canvas
    canvas = np.zeros_like(frame)

# Inisialisasi kamera
cap = cv2.VideoCapture(0)
prev_x, prev_y = None, None  # Koordinat sebelumnya untuk menggambar lebih halus

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    # Inisialisasi canvas jika belum ada
    if canvas is None:
        reset_gambar(frame)

    # Deteksi tangan
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hasil = hands.process(frame_rgb)

    if hasil.multi_hand_landmarks:
        for hand_landmarks in hasil.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Ambil koordinat ujung jari telunjuk
            x1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * frame.shape[1])
            y1 = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * frame.shape[0])

            # Pilih warna berdasarkan posisi jari telunjuk
            pilih_warna(x1, y1)

            # Gambar garis jika tidak sedang menghapus
            if prev_x is not None and prev_y is not None and not is_erasing:
                gambar_tangan((prev_x, prev_y), (x1, y1))

            # Simpan posisi jari telunjuk sebelumnya
            prev_x, prev_y = x1, y1
    else:
        prev_x, prev_y = None, None

    # Tampilkan pilihan warna
    cv2.rectangle(frame, (0, 0), (50, 50), (0, 0, 255), -1)  # Merah
    cv2.rectangle(frame, (50, 0), (100, 50), (0, 255, 0), -1)  # Hijau
    cv2.rectangle(frame, (100, 0), (150, 50), (255, 0, 0), -1)  # Biru

    # Gabungkan frame dengan canvas
    frame = cv2.addWeighted(frame, 0.5, canvas, 0.5, 0)

    # Tampilkan hasil
    cv2.imshow('Gambar dengan Tangan', frame)

    # Tombol untuk keluar atau hapus
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('r'):
        reset_gambar(frame)

cap.release()
cv2.destroyAllWindows()