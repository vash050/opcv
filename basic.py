import cv2 as cv

img = cv.imread("source/photos/park.jpg")
cv.imshow("Boston", img)

# Converting to grayscale
# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("boston gray", gray)

# Blur
# blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
# cv.imshow("boston blur", blur)

# Edge Cascade
# canny = cv.Canny(blur, 125, 175)
# cv.imshow("Boston canny", canny)

# Dilating the image
# dilated = cv.dilate(canny, (9, 9), iterations=3)
# cv.imshow("Boston dilated", dilated)

# Eroding the image
# eroded = cv.erode(dilated, (9, 9), iterations=3)
# cv.imshow("Boston eroded", eroded)

# Resize
# resized = cv.resize(
#     img, (img.shape[1] * 2, img.shape[0] * 2), interpolation=cv.INTER_CUBIC
# )
# cv.imshow("Boston resized", resized)


# Cropping
cropped = img[50:200, 200:400]
cv.imshow("Boston cropped", cropped)

cv.waitKey(0)
