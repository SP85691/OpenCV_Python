import cv2 as cv
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv.VideoCapture("Videos/japan.mp4")
# cap = cv.VideoCapture(0)

cTime = 0
pTime = 0

while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)
            cx, cy = int(lm.x*w), int(lm.y*h)
            cv.circle(img, (cx,cy), 1, (0, 255, 0), cv.FILLED)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv.putText(img, str(int(fps)), (70, 50), cv.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 4)

    cv.imshow("Posture",img)
    cv.waitKey(1)