# import cv2
# use cap variables to store videocapture
# condition
# success, image stores cap.read()
# dispalying cv2.imshow()
# condition
# if cv2.waitKey() & 0xFF== ('q')
# break
# webcam
# cap.set(0,640)
# cap.set(0,480)
# import cv2
import cv2
# store data in cap variable
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)
# condition
while True:
    # storing of variables in cap.read
    success, img = cap.read()
    # displaying
    cv2.imshow("videos", img)
    # condition
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break