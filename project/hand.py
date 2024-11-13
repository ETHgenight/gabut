import cv2
import mediapipe as mp

# Inisialisasi Mediapipe dan OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2)
mp_draw = mp.solutions.drawing_utils

# Membuka kamera
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    # Jika ada tangan yang terdeteksi
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Gambar landmark tangan
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Tampilkan hasil deteksi
    cv2.imshow("Deteksi Tangan", img)

    # Jika tekan 'q', keluar dari program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
