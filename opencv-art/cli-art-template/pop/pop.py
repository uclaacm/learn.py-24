import cv2

def popify_image(image, background_color=[255, 255, 255], dot_color=(0, 0, 0), max_dots=120):   
    """
    popify_image takes an input image and transforms it into a "pop art" version with the specified color parameters

    :param image: the image to transform - cv2.typing.MatLike
    :param background_color: background color for output image - list(r, g, b)
    :param dot_color: dot color for output image - tuple(r, g, b)
    :param max_dots: the maximum number of dots to include in the image - int
    :return: transformed image - cv2.typing.MatLike
    """ 

    # TODO: Convert the image to grayscale

    # Extract image dimensions
    image_height, image_width = image.shape

    # Down size image to the number of dots
    if image_height == max(image_height,image_width):
        downsized_image = cv2.resize(image,(int(image_height*(max_dots/image_width)),max_dots))
    else:
        downsized_image = cv2.resize(image,(max_dots,int(image_height*(max_dots/image_width))))

    # Extract dimensions of new image
    downsized_image_height, downsized_image_width = downsized_image.shape

    multiplier = 100

    # TODO: Set the blank_img_height, blank_img_width to the downsized image values * multiplier

    # TODO: Set the padding value to the floor of the multiplier divided by 2 
    padding = 0

    # TODO: use np.full(...) to create an empty 3D array with blank_img height and width, and 3 channels. 
    # Fill the array with the background_color as a parameter to np.full(). Store the result in blank_image
    blank_image = image

    # TODO: Loop through each index of the image height
        # TODO: Loop through each index of the image width
            # TODO: Draw a circle using cv2.circle(...) with the following parameters
            # - Provide the blank image
            # - The coordinates for the center of the circle should be the height and width index (as x and y respectively) each
            # multiplied by multiplier, and added to padding
            # - Set the radius of the circle to int((0.6 * multiplier) * ((255-downsized_image[y][x])/255))
            # Note: this sets the base size to (0.6 * multiplier) and scales it by the intensity of the raw downsized image.
            # - Provide the dot_color
            # 

    return blank_image
