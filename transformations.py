import cv2 as cv
import numpy as np

img = cv.imread("source/photos/park.jpg")


# Translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# -x --> Left
# -y --> Up
# x --> Right
# y --> Down
translate = translate(img, -100, 100)


# Rotation
def rotate(img, angle, center=None):
    (height, width) = img.shape[:2]

    if center is None:
        center = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(center, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)


# rotated = rotate(img, 45)
# cv.imshow("Translated", translate)
# cv.imshow("Rotated", rotated)
flip = cv.flip(img, 0)  # flipCode horiz 1, vertical 0, both -1
cv.imshow("Flipped", flip)
cv.waitKey(0)
