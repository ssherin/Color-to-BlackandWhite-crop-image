import cv2
#import numpy as pd

img = cv2.imread("Iron.png")

cv2.imshow("Original",img)

cv2.waitKey(0)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gray scale image", gray_img)
#cv2.waitKey(0)
img_scaled = cv2.resize(gray_img, None, fx =0.40, fy=0.40)
cv2.imshow("Scaling",img_scaled)
cv2.waitKey()

cv2.destroyAllWindows()