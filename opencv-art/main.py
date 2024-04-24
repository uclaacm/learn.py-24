import cv2
import argparse
from pointillism import pointillism
from pop import pop

valid_ops = ["oil-painting", "watercolor", "cartoon", "sketch-bw", "sketch-c", "pop", "pointillism"]

parser = argparse.ArgumentParser(description='...')
parser.add_argument('img_path', nargs='?', default="images/ucla.jpg")
for op in valid_ops:
    parser.add_argument(f"--{op}", dest="ops", action="append_const", const=op)
parser.add_argument("--all", dest="ops", action="store_const", const=valid_ops)
parser.add_argument("--display", dest="display", action="store_true")

args = parser.parse_args()

img = cv2.imread(args.img_path)    
for op in args.ops or [valid_ops[0]]:
    if (op == "oil-painting"):
        res = cv2.xphoto.oilPainting(img, 7, 1)

    elif (op == "watercolor"):
        res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)

    elif (op == "cartoon"):
        res = cv2.medianBlur(img, 7)

    elif (op == "sketch-bw"):
        res, _ = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 
        
    elif (op == "sketch-c"):
        _, res = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05) 

    elif (op == "pop"):
        res = pop.popify_image(img, background_color=[255, 255, 255], dot_color=(0, 0, 0))

    elif (op == "pointillism"):
        res = pointillism.draw_pointillism(img, palette_size=20, stroke_scale=0, grad_smoothing_radius=0)

    if (args.display):
        cv2.imshow("res", res)

    res_path = args.img_path.rsplit(".", -1)[0] + f"-{op}-drawing.png"
    cv2.imwrite(res_path, res)
    cv2.waitKey(0)