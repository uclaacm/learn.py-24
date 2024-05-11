import numpy as np

# Adapted from https://github.com/uclaacm/learn.py-s21/tree/main/session-8-standard-library-and-packages#opencv-demo-time-a-professional-meme-deep-fryer
def fry_image(src_img, contrast = 2.2, brightness = 50):
    """
    fry_image takes an input image and transforms it into a "deep fried" version with the specified formatting parameters

    :param src_img: the image to transform - cv2.typing.MatLike
    :param contrast: contrast for output image - int
    :param brightness: brightness of the output image - int
    :return: transformed image - cv2.typing.MatLike
    """ 

    img = src_img.copy()

    ## Loop through our image to increaset the sharpness of it (first blur, then subtract blur from original)
    for _ in range(10):
        # TODO: Perform gaussian blur with 3x3 kernel and Sigma X of 13 and store in `frame`

        # TODO: Use the addWeighted() function, to apply the frame to `img` with alpha: 1.5, beta: -0.5, gamma: 0 (remove next line)
        pass

    ## Adding red hue to image
    # TODO: Split the image into color channels (remove next line)
    b = g = r = None

    r = r*contrast + brightness
    r = r.astype(np.uint8)
    r = np.clip(r, 0, 255)

    # TODO: Merge the color channels into a single image `img`

    ## Detect edges, then strengthen these edges with red and overlay them over image
    # TODO: Create a Canny filter with thresholds of 50 called `edges`
    edges = None

    red_edges = np.zeros(img.shape)
    red_edges[:, :, 2] = edges
    red_edges = red_edges.astype(np.uint8)

    # TODO: Use the addWeighted() function, to apply the frame to `img` with alpha: 0.5, beta: 0.5, gamma: 0

    ## Increase the brightness of the image
    img = img*1.5 + 50
    img = img.astype(np.uint8)

    return img