import cv2 as cv
import mediapipe as mp
import time

class poseDetector():
    
    def __init__(self, mode=False, upBody = False, smooth = True, detection = 0.5, trackcon = 0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detection = detection
        self.trackcon = trackcon
        
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detection, self.trackcon)

    def findPose(self, img, draw=True):

        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
    
        return img

    def GetPose(self, img, draw = True):
        lmlist = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmlist.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx,cy), 5, (255, 0, 0), cv.FILLED)
        return lmlist


def main():
    cap = cv.VideoCapture("Videos/run.mp4")
    # cap = cv.VideoCapture(0)

    detector = poseDetector()
    cTime = 0
    pTime = 0

    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmlist = detector.GetPose(img, draw=False)
        if len(lmlist) !=0:
            print(lmlist)
            cv.circle(img, (lmlist[14][1], lmlist[14][2]), 15, (255, 0, 255), cv.FILLED)


        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (50, 70), cv.FONT_HERSHEY_PLAIN, 5, (255, 0, 255), 4)

        cv.imshow("Posture",img)
        cv.waitKey(1)


if __name__ == "__main__":
    main()