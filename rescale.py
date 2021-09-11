#Import The Necessary LIBRARY
import cv2 as cv

#Read The Given file

# ########## ANALYZING IMAGE ##########

# img = cv.imread("Photos/pic4.jpg")
# cv.imshow("Image",img)      

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    dimension = (width,height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    #LIVE VIDEO
    cap.set(3,width)
    cap.set(4,height)

# resize = rescaleFrame(img, scale=2)
# cv.imshow("RESIZED IMAGE", resize)

########### Resized FOR VIDEOS ##############

cap = cv.VideoCapture("Videos/elon1.mp4")
# cap = cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()
    frame_resized = rescaleFrame(frame)
    # change_res = changeRes(frame)
    cv.imshow("Videos",frame)
    cv.imshow("Video Rescaled", frame_resized)
    # cv.imshow("Changed Resolution", change_res)
    if cv.waitKey(20) & 0xff==ord('q'):
        break 

cap.release()
cv.destroyAllWindows()         