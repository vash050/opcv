import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("source/videos/output.avi", fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Camera", frame)
    out.write(frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
out.release()
cv.destroyAllWindows()
