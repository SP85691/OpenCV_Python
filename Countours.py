import cv2 as cv
import numpy as np

img = cv.imread("Photos/jujutsu.jpg") # 610 x 1260 px
img_res = cv.resize(img,(500, 920), interpolation=cv.INTER_CUBIC)
# cv.imshow("Image", img_res)
cv.imshow("Image", img_res)

blank = np.zeros(img_res.shape, dtype = 'uint8')
cv.imshow("Blank", blank)

#Gray Scale OF IMAGE
imgGray = cv.cvtColor(img_res, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", imgGray)

#Canny Image 
imgCanny = cv.Canny(img_res, 125, 175)
cv.imshow("Canny", imgCanny)

#Threshold Image
# ret, thresh = cv.threshold(imgGray, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Thresh Image", thresh)

#Contours the Image
contours, hierarchy = cv.findContours(imgCanny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# --------------- DRAW CONTOURS ---------------- #
cv.drawContours(blank, contours, -1, (0, 0, 200), 1)
cv.imshow("Contours Draw", blank)


cv.waitKey(0)