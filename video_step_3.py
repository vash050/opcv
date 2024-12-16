import cv2 as cv

frames = []

cap = cv.VideoCapture("source/videos/output.avi")
# 1 чтение изображений
while True:
    ret, img = cap.read()
    if not ret:
        break
    frames.append(img)


# Функция для ползунка
def nothing(arg):
    pass


cv.namedWindow("video")
# Создание ползунка
cv.createTrackbar("frame_number", "video", 0, len(frames) - 1, nothing)

# Отображение выбранного
while True:
    frame_number = cv.getTrackbarPos("frame_number", "video")
    print(frame_number)
    img = frames[frame_number]
    cv.imshow("video", img)
    if cv.waitKey(33) & 0xFF == ord("q"):
        break
cv.destroyAllWindows()
