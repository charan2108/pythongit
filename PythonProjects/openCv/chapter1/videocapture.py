import cv2

cap = cv2.VideoCapture('videos/PredatorB.wmv')

while True:
    success, img= cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break