import cv2
import numpy as np
img= cv2.imread("oyku.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Bne", img)
cv2.imshow("Gri bne", gray)
print(img)
cv2.waitKey(0)
cv2.destroyWindow()