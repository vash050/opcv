import cv2 as cv

img = cv.imread("source/photos/park.jpg")
cv.imshow("Boston", img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Boston gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("Boston HSV", hsv)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Boston LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("Boston RGB", rgb)

# HSV to RGB
rgb_from_hsv = cv.cvtColor(hsv, cv.COLOR_HSV2RGB)
cv.imshow("Boston RGB from HSV", rgb_from_hsv)

# HSV to BGR
bgr_from_hsv = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow("Boston BGR from HSV", bgr_from_hsv)

# LAB to BGR
bgr_from_lab = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("Boston BGR from LAB", bgr_from_lab)

cv.waitKey(0)
