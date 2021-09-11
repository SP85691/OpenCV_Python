import cv2 as cv
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode = False, MaxHands = 2, DetectionCon = 0.5, TrackCon = 0.5):
        self.mode = mode
        self.MaxHands = MaxHands
        self.DectectionCon = DetectionCon
        self.TrackCon = TrackCon    

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.MaxHands, self.DectectionCon, self.TrackCon)
        self.mpDraw = mp.solutions.drawing_utils   

    def FindHANDS(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        # print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handlms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handlms, self.mpHands.HAND_CONNECTIONS)

        return img


    def FindPosition(self, img, HandNo = 0, draw = True):

        lmlist  = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[HandNo]
            for id, lm in enumerate(myHand.landmark):
                    # print(id, lm)
                    h, w, s = img.shape
                    cx, cy = int(lm.x*w), int(lm.y*h)
                    # print(id, cx,cy)
                    lmlist.append([id, cx, cy])
                    if draw:
                        cv.circle(img, (cx, cy), 7, (255, 0, 0), cv.FILLED)
        return lmlist

def main():
    cap = cv.VideoCapture(0)

    cTime = 0
    pTime = 0

    detector = HandDetector()

    while True:
        success, img =cap.read()

        img = detector.FindHANDS(img)
        lmlist = detector.FindPosition(img, draw=False)
        if len(lmlist) != 0:
            print(lmlist[4])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10,70), cv.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)


        cv.imshow("Image",img)
        cv.waitKey(1)

if __name__ == "__main__":
    main()