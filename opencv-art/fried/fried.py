import cv2
import numpy as np
import progressbar as pb

def fry_image(src_img, contrast = 2.2, brightness = 50):
    img = src_img.copy()
    for _ in range(10):
        frame = cv2.GaussianBlur(img, (3,3), 13)
        img = cv2.addWeighted(img, 1.5, frame, -0.5, 0)

    b, g, r = cv2.split(img)
    r = r*contrast + brightness
    r = r.astype(np.uint8)
    r = np.clip(r, 0, 255)
    img = cv2.merge((b, g, r))

    edges = cv2.Canny(img, 50, 50)
    red_edges = np.zeros(img.shape)
    red_edges[:, :, 2] = edges
    red_edges = red_edges.astype(np.uint8)
    img = cv2.addWeighted(img, 0.5, red_edges, 0.5, 0)

    img = img*1.5 + 50
    img = img.astype(np.uint8)

    return img