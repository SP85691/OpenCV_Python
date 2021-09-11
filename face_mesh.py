import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture("Videos/songs.mp4")
pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces = 5)
drawSpec = mpDraw.DrawingSpec(thickness = 1, circle_radius = 2)


while True:
    success, img = cap.read()
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for faceLMS in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLMS, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img, f'FPS: {int(fps)}', (28, 78), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

    cv.imshow("Image",img)
    cv.waitKey(20)
