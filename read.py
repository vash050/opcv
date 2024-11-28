import cv2 as cv

# img = cv.imread("source/photos/cat.jpg")
#
# cv.imshow("Cat", img)

capture = cv.VideoCapture("source/videos/dog.mp4")

while True:
    ret, frame = capture.read()

    if not ret:
        break

    cv.imshow("Video", frame)

    if cv.waitKey(33) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
