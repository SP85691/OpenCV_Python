import cv2 as cv

img = cv.imread("Photos/pic2.jpg")
cv.imshow("Image", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# SIMPLE THRESHOLDING
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Simple Threshold", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Simple Threshold Inverse", thresh_inv)

# ADAPTIVE THRESHOLD
adapt_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 99, 10)
cv.imshow("Adaptive Threshold", adapt_thresh)
print(cv.adaptiveThreshold)

cv.waitKey(0)