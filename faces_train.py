import os
import cv2 as cv
import numpy as np


people = ["ben_afflek", "elton_john", "jerry_seinfeld", "madonna", "mindy_kaling"]

# p = []
# for i in os.listdir(r"/home/vasiliy/projects/opencv/learn_1/opcv/source/train"):
#     p.append(i)
#
# print(p)
DIR = r"/home/vasiliy/projects/opencv/learn_1/opcv/source/train"

haar_cascade = cv.CascadeClassifier("source/haar_face.xml")

features = []
labels = []


def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            img = cv.imread(img_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=4,
            )

            for x, y, w, h in faces_rect:
                face_roi = gray[y : y + h, x : x + w]
                features.append(face_roi)
                labels.append(label)


create_train()
print(f"Training done ----------------")
features = np.array(features, dtype="object")
labels = np.array(labels)

# print(f"Length of training {len(features)}")
# print(f"Length of training {len(labels)}")

faces_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the Recognizer on the features list and the labels list
faces_recognizer.train(features, labels)
faces_recognizer.save("source/save_np/face_trained.yml")

np.save("source/save_np/features.npy", features)
np.save("source/save_np/labels.npy", labels)
