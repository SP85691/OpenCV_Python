import cv2 as cv
import numpy as np

#PATH OF THE IMAGE
img = cv.imread("Photos/buston.jpg")
cv.imshow("Image", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

#SPLITTED IMAGE
r,g,b = cv.split(img)

#Merge Them
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Red", red)
cv.imshow("Green", green)
cv.imshow("Blue", blue)

#SIZE OF IMAGE
print(img.shape)
print(r.shape)
print(g.shape)
print(b.shape)

#MERGED IMAGE
merged = cv.merge([r,g,b])
cv.imshow("Merged Image", merged)
print(merged.shape)

cv.waitKey(0)