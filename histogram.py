#importing the libraries
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/pic2.jpg")
cv.imshow("Image", img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray Scale", gray)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("Blank", blank)

# Making A Masked Image
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)

# MASK
masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)

# -------- Gray - Sacle HistoGram ----------- #
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256]) 

# plt.figure()
# plt.title("Masked Gray-Scale HistoGram")
# plt.xlabel("Bins")
# plt.ylabel("# of pixles")
# plt.plot(gray_hist)
# plt.xlim([0, 256])
# plt.show()

# -------- Color Image - Sacle HistoGram ----------- #
plt.figure()
plt.title("Color Image - Sacle HistoGram")
plt.xlabel("Bins")
plt.ylabel("# of pixles")

color = ('b', 'g', 'r')
for i, col in enumerate(color):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)

 