import cv2
import argparse
import math
import progressbar
from pointillism import *

parser = argparse.ArgumentParser(description='...')
parser.add_argument('img_path', nargs='?', default="images/ucla.jpg")

args = parser.parse_args()

res_path = args.img_path.rsplit(".", -1)[0] + "_drawing.png"
img = cv2.imread(args.img_path)
    
res = cv2.xphoto.oilPainting(img, 7, 1)

cv2.imshow("res", limit_size(res, 1080))
cv2.imwrite(res_path, res)
cv2.waitKey(0)