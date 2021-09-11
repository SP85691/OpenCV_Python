import cv2 as cv
import numpy as np

img = cv.imread("Photos/pic2.jpg")
# img_res = cv.resize(img, (500,800), interpolation=cv.INTER_AREA)
cv.imshow("Smilly", img)

# Averaging Blur
average = cv.blur(img, (7,7))
cv.imshow("Average Blur", average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Image Gaussion", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median)

# Bilateral Blurring
bil_blur = cv.bilateralFilter(img, 5, 35, 40)
cv.imshow("Bilateral Blur", bil_blur)

cv.waitKey(0)