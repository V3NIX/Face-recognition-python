import time

import cv2
import numpy as np
import face_recognition
import os
import joblib

path = 'persons'
images = []
classNames = []
personsList = os.listdir(path)


# Load the pre-trained SVM model
clf = joblib.load('svm_model.joblib')

# Load the face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
print('SVM loaded successfully.')



for cl in personsList:
    curPersonn = cv2.imread(f'{path}/{cl}')
    images.append(curPersonn)
    classNames.append(os.path.splitext(cl)[0])


def findEncodeings(image):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodeings(images)
print('Encoding Complete.')

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture('./source/access_granted.jpeg')
cap2 =cv2.VideoCapture('./source/access_denied.jpeg')


while True:
    ret, img = cap.read()

    if ret:  # ensure that the input image is not empty
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurentFrame = face_recognition.face_locations(imgS)
        encodeCurentFrame = face_recognition.face_encodings(imgS, faceCurentFrame)

        for encodeface, faceLoc in zip(encodeCurentFrame, faceCurentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeface)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeface)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                ret, frame = cap1.read()
                if ret:
                    cv2.imshow("Known Face!", frame)
                    cv2.waitKey(3000)
                    cv2.destroyWindow("Known Face!")

            else:
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
                cv2.putText(img, 'uknown', (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                ret, frame = cap2.read()
                if ret:
                    cv2.imshow("Unknown Face!", frame)
                    cv2.waitKey(3000)
                    cv2.destroyWindow("Unknown Face!")

        cv2.imshow('Face Recognition', img)
        if cv2.waitKey(1) & 0xFF == 27:
            break
cap.release()
cap1.release()
cap2.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
