import cv2
import argparse
from pop import pop
import util
from fried import fried

valid_ops = ["oil-painting", "fried", "pop"]

# Creating ArgumentParser and adding path and display
parser = argparse.ArgumentParser(description='...')
parser.add_argument('img_path', nargs='?', default="images/ucla.jpg")
parser.add_argument("--display", dest="display", action="store_true")

# Looping through valid transformation operations and adding them as arguments
for op in valid_ops:
    parser.add_argument(f"--{op}", dest="ops", action="append_const", const=op)
parser.add_argument("--all", dest="ops", action="store_const", const=valid_ops)

args = parser.parse_args()
img = cv2.imread(args.img_path)

# Looping through provided operations (or by default just the first operation)
for op in args.ops or [valid_ops[0]]:
    if (op == "oil-painting"):
        res = cv2.xphoto.oilPainting(img, 7, 1)

    elif (op == "pop"):
        res = pop.popify_image(img)

    elif (op == "fried"):
        res = fried.fry_image(img)

    # Displaying transformed image if arg is present
    if (args.display):
        cv2.imshow("res", util.limit_size(res, 1080))

    # Formatting output file path
    file_name = args.img_path.split(".")[0].split('/')[-1]
    res_path = f"./output/{file_name}-{op}-drawing.png"

    # Writing out image
    cv2.imwrite(res_path, res)