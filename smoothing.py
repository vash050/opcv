import cv2 as cv

img = cv.imread("source/photos/cats.jpg")
cv.imshow("Cats", img)

# Average
avg = cv.blur(img, (3, 3))
cv.imshow("Cats Average", avg)

# Gaussian
gaussian = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Cats Gaussian", gaussian)

# Median
median = cv.medianBlur(img, 3)
cv.imshow("Cats Median", median)

# Bilateral
bilateral = cv.bilateralFilter(img, 15, 35, 25)
cv.imshow("Cats Bilateral", bilateral)

cv.waitKey(0)
