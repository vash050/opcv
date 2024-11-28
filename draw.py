import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype="uint8")
# cv.imshow("Blank", blank)

# 1. Paint the image a certain colour
# blank[:] = 0, 255, 0
# cv.imshow("Green", blank)

# 2. Red square the image
# blank[200:300, 300:400] = 0, 0, 255
# cv.imshow("Green", blank)

# 3. draw a rectangle
# cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=5)
# cv.rectangle(blank, (0, 0), (250, 500), (0, 255, 0), thickness=-1)
# cv.rectangle(
#     blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness=-1
# )
# cv.imshow("Rectangle", blank)

# 4. Draw a circle
# cv.circle(blank, (250, 250), 100, (0, 255, 0), thickness=5)
# cv.imshow("Circle", blank)

# 5. Draw a line
# cv.line(blank, (50, 50), (150, 150), (0, 255, 0), thickness=2)
# cv.line(blank, (150, 150), (50, 450), (0, 255, 0), thickness=2)
# cv.line(blank, (50, 450), (150, 475), (0, 255, 0), thickness=2)
# cv.line(blank, (150, 475), (450, 50), (0, 255, 0), thickness=2)
# cv.imshow("Line", blank)

# 6. write text
cv.putText(
    blank, "Hello", (100, 100), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=1
)
cv.imshow("Text", blank)

# img = cv.imread("source/photos/cat.jpg")
#
# cv.imshow("Cat", img)

cv.waitKey(0)
