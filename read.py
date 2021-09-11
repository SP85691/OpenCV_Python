#Import The Necessary LIBRARY
import cv2 as cv

#Read The Given file

# ########## ANALYZING IMAGE ##########

img = cv.imread("Photos/pic2.jpg")
cv.imshow("Image",img)
 
#Gray the Image
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Image GRAYSCALE",imgGray)

#Blur the Image
imgBlur = cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT )
cv.imshow("Image Blur", imgBlur)

#Canny The Image
imgCanny = cv.Canny(img, 125, 175)
cv.imshow("Canny image", imgCanny)

#Dilate the Image
imgDil = cv.dilate(imgCanny, (3,3), iterations=2)
cv.imshow("Dialtion Image", imgDil)

#Erode The Image
imgErode = cv.erode(imgDil, (5,5), iterations=1)
cv.imshow("Erorded", imgErode)

#Resizing The Image
imgResize = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", imgResize)

#CROPPING THE IMAGE
imgCropped = img[50:200, 200:400]
cv.imshow("Cropped", imgCropped)
cv.waitKey(0)                       #--> Using waitKey as 0 for infinte




########## ANALYZING VIDEO ##########

# # cap = cv.VideoCapture("Videos/elon1.mp4")
# cap = cv.VideoCapture(0)
# while True:
#     isTrue, frame = cap.read()
#     cv.imshow("Videos",frame)
#     if cv.waitKey(20) & 0xff==ord('q'):
#         break 

# cap.release()
# cv.destroyAllWindows()
          