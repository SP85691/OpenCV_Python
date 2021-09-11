import os
import cv2 as cv
import numpy as np


people = ["RDJ", "mark", "chris"]
DIR = r'C:\Users\Surya Pratap\OneDrive\Desktop\OpenCV_Projects\AI_Train'

haar_cascade = cv.CascadeClassifier("haar_faces.xml")


features = []
labels = []

def creat_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# create_train()
print("Face Recognizer Trained -----------------")
# print(f"Length of the Features = {len(features)}")
# print(f"Length of the Labels = {len(labels)}")

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Face Recognizer
face_recognizer.train(features, labels)

np.save('feature.npy', features)
np.save('labels.npy', labels)



# -------------- FIRST WAY TO DO ----------------- ###

# p = []

# for i in os.listdir(r'C:\Users\Surya Pratap\OneDrive\Desktop\OpenCV_Projects\AI_Train'):
#     p.append(i)

# print(p)