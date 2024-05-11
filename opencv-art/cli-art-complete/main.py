import cv2
import argparse
from pointillism import pointillism, utils
from pop import pop
from fried import fried

valid_ops = ["oil-painting", "watercolor", "cartoon", "fried", "sketch-bw", "sketch-c", "pop", "pointillism"]

parser = argparse.ArgumentParser(description='...')
parser.add_argument('img_path', nargs='?', default="images/ucla.jpg")
for op in valid_ops:
    parser.add_argument(f"--{op}", dest="ops", action="append_const", const=op)
parser.add_argument("--all", dest="ops", action="store_const", const=valid_ops)

parser.add_argument("--display", dest="display", action="store_true")

parser.add_argument("-s", "--sigma-s", default=60, dest="sigma_s")
parser.add_argument("-r", "--sigma-r", default=0.15, dest="sigma_r")
parser.add_argument("-w", "--watercolor-r", default=0.6, dest="watercolor_r")
parser.add_argument("-f", "--shade-factor", default=0.05, dest="shade_factor")
parser.add_argument("-b", "--brush-size", default=7, dest="brush_size")

args = parser.parse_args()

img = cv2.imread(args.img_path)    
for op in args.ops or [valid_ops[0]]:
    if (op == "oil-painting"):
        res = cv2.xphoto.oilPainting(img, args.brush_size, 1)

    elif (op == "watercolor"):
        res = cv2.stylization(img, sigma_s=args.sigma_s, sigma_r=args.watercolor_r)

    elif (op == "cartoon"):
        res = cv2.medianBlur(img, args.brush_size)

    elif (op == "sketch-bw"):
        res, _ = cv2.pencilSketch(img, sigma_s=args.sigma_s, sigma_r=args.sigma_r, shade_factor=args.shade_factor) 
        
    elif (op == "sketch-c"):
        _, res = cv2.pencilSketch(img, sigma_s=args.sigma_s, sigma_r=args.sigma_r, shade_factor=args.shade_factor) 

    elif (op == "pop"):
        res = pop.popify_image(img, background_color=[255, 255, 255], dot_color=(0, 0, 0))

    elif (op == "pointillism"):
        res = pointillism.draw_pointillism(img, palette_size=20, stroke_scale=0, grad_smoothing_radius=0)

    elif (op == "fried"):
        res = fried.fry_image(img)

    if (args.display):
        cv2.imshow("res", utils.limit_size(res, 1080))

    file_name = args.img_path.split(".")[0].split('/')[-1]
    res_path = f"./output/{file_name}-{op}-drawing.png"
    cv2.imwrite(res_path, res)
    cv2.waitKey(0)