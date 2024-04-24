import cv2
import argparse
import math
import progressbar
from pointillism import *

valid_ops = ["oil-painting", "watercolor", "sketch-bw", "sketch-c"]

parser = argparse.ArgumentParser(description='...')
parser.add_argument('img_path', nargs='?', default="images/ucla.jpg")
for op in valid_ops:
    parser.add_argument(f"--{op}", dest="ops", action="append_const", const=op)

args = parser.parse_args()

img = cv2.imread(args.img_path)    
for op in args.ops:
    if (op == "oil-painting"):
        res = cv2.xphoto.oilPainting(img, 7, 1)

    elif (op == "watercolor"):
        res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

    elif (op == "sketch-bw"):
        res, _ = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
        
    elif (op == "sketch-c"):
        _, res = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    cv2.imshow("res", limit_size(res, 1080))

    res_path = args.img_path.rsplit(".", -1)[0] + f"-{op}-drawing.png"
    cv2.imwrite(res_path, res)
    cv2.waitKey(0)