import cv2
import numpy as np
import os
from datetime import datetime

# Folder berisi gambar wajah karyawan yang dikenal
path = 'images'
images = []
classNames = []
myList = os.listdir("javas")

# Membaca gambar dan mendapatkan nama
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])

# Membuat recognizer untuk wajah menggunakan LBPH (Local Binary Patterns Histogram)
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Fungsi untuk menandai kehadiran
def mark_attendance(name):
    with open('attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%Y-%m-%d %H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            print(f'{name} telah ditandai hadir pada {dtString}')

# Melatih model menggunakan gambar yang ada
def train_model(images, classNames):
    gray_images = []
    labels = []
    for idx, img in enumerate(images):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray_images.append(gray)
        labels.append(idx)
    face_recognizer.train(gray_images, np.array(labels))

# Melatih model
train_model(images, classNames)
print('Training Complete')

# Membuka kamera untuk menangkap wajah secara real-time
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]

        # Mencocokkan wajah
        label, confidence = face_recognizer.predict(roi_gray)

        if confidence < 100:
            name = classNames[label].upper()
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            mark_attendance(name)
        else:
            cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

