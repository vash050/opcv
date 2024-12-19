import cv2 as cv
import numpy as np


haar_cascade = cv.CascadeClassifier("source/haar_face.xml")

people = ["ben_afflek", "elton_john", "jerry_seinfeld", "madonna", "mindy_kaling"]
# features = np.load("source/save_np/features.npy", allow_pickle=True)
# labels = np.load("source/save_np/labels.npy")

faces_recognizer = cv.face.LBPHFaceRecognizer_create()
faces_recognizer.read("source/save_np/face_trained.yml")

img = cv.imread(
    r"source/val/madonna/httpcdncdnjustjaredcomwpcontentuploadsheadlinesmadonnatalksparisattackstearsjpg.jpg"
)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Person", gray)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for x, y, w, h in faces_rect:
    face_roi = gray[y : y + h, x : x + w]
    label, confidence = faces_recognizer.predict(face_roi)

    print(f"Label: {label}, Confidence: {confidence}")

    if confidence >= 50:
        label_name = people[label]
    else:
        label_name = "Unknown"

    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv.putText(
        img, label_name, (20, 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2
    )

cv.imshow("Detected faces", img)
cv.waitKey(0)
