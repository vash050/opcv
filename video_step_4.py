import cv2 as cv

g_slider_position = 0

cap = cv.VideoCapture("source/videos/output.avi")
frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))


def nothing(arg):
    pass


cv.namedWindow("slider")
cv.createTrackbar("frame_number", "slider", 0, frame_count - 1, nothing)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frame_number = cv.getTrackbarPos("frame_number", "slider")
    print(f"number: {frame_number}")
    cv.setTrackbarPos("frame_number", "slider", g_slider_position)
    print(g_slider_position)
    g_slider_position += 1

    cv.imshow("slider", frame)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv.waitKey(30) & 0xFF == ord("p"):
        print("Paused")
        while True:
            if cv.waitKey(0) & 0xFF == ord("p"):
                print("Unpaused")
                break
            if cv.waitKey(0) & 0xFF == ord("b"):
                g_slider_position += 1
                cv.setTrackbarPos("frame_number", "slider", g_slider_position)
                cv.imshow("slider", frame)
                print(g_slider_position)

cv.destroyAllWindows()
