import cv2 
img = cv2.imread("learn_py.png")
img = cv2.rectangle(img, (10, 270), (140, 100), 
                    (255, 0, 0), 2)

 
cv2.imshow("Display window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
