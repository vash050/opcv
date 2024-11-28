import cv2 as cv


def rescale_frame(frame, scale=0.75):
    # Images, Videos and Live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    res = (width, height)
    return cv.resize(frame, res, interpolation=cv.INTER_AREA)


def change_res(width, height):
    # Live videos
    capture.set(3, width)
    capture.set(4, height)


capture = cv.VideoCapture("source/videos/dog.mp4")

while True:
    ret, frame = capture.read()

    if not ret:
        break

    frame_resized = rescale_frame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Resized Video", frame_resized)

    if cv.waitKey(33) & 0xFF == ord("q"):
        break

capture.release()
cv.destroyAllWindows()
