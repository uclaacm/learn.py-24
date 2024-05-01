import numpy as np
import math
import cv2
import progressbar as pb
from .vector_field import VectorField
from .color_palette import ColorPalette
from .utils import randomized_grid, compute_color_probabilities, color_select

def draw_pointillism(img, palette_size=20, stroke_scale=0, grad_smoothing_radius=0):
    if stroke_scale == 0:
        stroke_scale = int(math.ceil(max(img.shape) / 1000))

    if grad_smoothing_radius == 0:
        grad_smoothing_radius = int(round(max(img.shape) / 50))

    # convert the image to grayscale to compute the gradient
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    palette = ColorPalette.from_image(img, palette_size)
    palette = palette.extend([(0, 50, 0), (15, 30, 0), (-15, 30, 0)])

    gradient = VectorField.from_gradient(gray)
    gradient.smooth(grad_smoothing_radius)

    # create a "cartonized" version of the image to use as a base for the painting
    res = cv2.medianBlur(img, 11)

    # define a randomized grid of locations for the brush strokes
    grid = randomized_grid(img.shape[0], img.shape[1], scale=3)
    batch_size = 10000

    bar = pb.ProgressBar(widgets=["Pointillism Image ", pb.Bar(), " ", pb.Percentage()])   
    for h in bar(range(0, len(grid), batch_size)):
        # get the pixel colors at each point of the grid
        pixels = np.array([img[x[0], x[1]] for x in grid[h:min(h + batch_size, len(grid))]])
        # precompute the probabilities for each color in the palette
        # lower values of k means more randomnes
        color_probabilities = compute_color_probabilities(pixels, palette, k=9)

        for i, (y, x) in enumerate(grid[h:min(h + batch_size, len(grid))]):
            color = color_select(color_probabilities[i], palette)
            angle = math.degrees(gradient.direction(y, x)) + 90
            length = int(round(stroke_scale + stroke_scale * math.sqrt(gradient.magnitude(y, x))))

            # draw the brush stroke
            cv2.ellipse(res, (x, y), (length, stroke_scale), angle, 0, 360, color, -1, cv2.LINE_AA)

    return res