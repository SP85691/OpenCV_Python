import cv2 as cv
import numpy as np

img = cv.imread("Photos/group.jpg")
# imgCanny = cv.Canny(img, 125, 175)
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img_res = cv.resize(img, (1080,640), interpolation=cv.INTER_AREA)
cv.imshow("Image", img)

# ----------------------- TRANSLATE THE IMAGE ------------------- #
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimension = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimension)

# -x --> Left
# -y --> Up
#  x --> Right
#  y --> Down

imgTrans = translate(img, 100, 100)
cv.imshow("Translated Image", imgTrans)

# ---------------- ROTATE THE IMAGE ------------------ #
def rotation(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)

imgRotate = rotation(img, -90)
cv.imshow("Rotated Image", imgRotate)

rotated = rotation(imgRotate, -45)
cv.imshow("ImRotated", rotated)

# ------------- FILPPING THE IMAGE ---------------- #

imgFlip = cv.flip(imgGray, 0)
cv.imshow("Flipped Image", imgFlip)

cv.waitKey(0)