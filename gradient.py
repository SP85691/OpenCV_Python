import cv2 as cv
import numpy as np

img = cv.imread("Photos/surya.jpg")
img_res = cv.resize(img, (500,800), interpolation=cv.INTER_AREA)
cv.imshow("Image", img_res)

gray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", gray)

# THRESHOLD
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow("Laplacium", lap)

# SOBEL
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)

cv.imshow("Sobel X", sobelx)
cv.imshow("Sobel Y", sobely)

# CANNY IMAGE OF GRAY IMAGE

canny = cv.Canny(gray, 150, 175)
cv.imshow("Canny Image", canny)

# COMBINE SOBEL X with SOBEL Y

combine = cv.bitwise_or(sobelx, sobely)
cv.imshow("Combined Sobel", combine)


cv.waitKey(0)