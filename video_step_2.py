import cv2 as cv
import numpy as np

frames = []
cap = cv.VideoCapture("source/videos/output.avi")
frame_count = int(cap.get(cv.CAP_PROP_FRAME_COUNT))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv.imshow("Video", frame)

    key = cv.waitKey(int(frame_count / 1000))
    if key & 0xFF == ord("p"):
        print("Paused")
        while True:
            key = cv.waitKey(0)
            if key & 0xFF == ord("p"):
                print("Unpaused")
                break

            if key & 0xFF == ord("b"):
                cur_frame_number = cap.get(cv.CAP_PROP_POS_FRAMES)
                print("* At frame #" + str(cur_frame_number))

                prev_frame = cur_frame_number
                if cur_frame_number > 1:
                    prev_frame -= 2

                print("* Rewind to frame #" + str(prev_frame))
                cap.set(cv.CAP_PROP_POS_FRAMES, prev_frame)

            if key & 0xFF == ord("r"):
                cap.set(cv.CAP_PROP_POS_FRAMES, 0)
                break

    elif cv.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv.destroyAllWindows()
