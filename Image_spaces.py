import cv2 as cv
import matplotlib.pyplot as plt

# ------------- NORMAL IMAGE --------------- #
img = cv.imread("Photos/pic2.jpg")
cv.imshow("Image", img)

# plt.imshow(img)
# plt.show()

# -------------- Gray Scale Image ---------- #
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# -------------- HSV Image ----------------- #
imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Image", imgHSV)

# -------------- Image BGR to LAB ----------------- #
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("Image LAB", lab)

# -------------- Image BGR to RGB ----------------- #
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("ImgRGB", rgb)

# -------------- HSV to BGR ----------------------- #
hsv_bgr = cv.cvtColor(imgHSV, cv.COLOR_HSV2BGR)
cv.imshow("HSV --> BGR", hsv_bgr)

# -------------- HSV to BGR ----------------------- #
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow("LAB --> BGR", lab_bgr)

# plt.imshow(hsv_bgr)
# plt.show()

cv.waitKey(0)

