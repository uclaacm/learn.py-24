import cv2 
img = cv2.imread("learn_py.png")
 
cv2.imshow("Display window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
