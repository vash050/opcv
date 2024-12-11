import cv2 as cv

img = cv.imread("source/photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Cats gray", gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Cats simple threshold", thresh)

threshold, thresh_inversion = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Cats simple inversion threshold", thresh_inversion)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(
    gray,
    255,
    cv.ADAPTIVE_THRESH_GAUSSIAN_C,
    cv.THRESH_BINARY_INV,
    11,
    9,
)
cv.imshow("Cats adaptive threshold", adaptive_thresh)


cv.waitKey(0)
