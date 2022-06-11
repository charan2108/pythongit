import cv2
print("Package imported")
 
# Images
img = cv2.imread("images/mobile.png")
cv2.imshow("Output",img)
cv2.waitKey(0)