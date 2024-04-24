import cv2
import numpy as np
import progressbar

def popify_image(image, background_color=[255, 255, 255], dot_color=(0, 0, 0), max_dots=120):
    # make image grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

    # extract dimensions
    image_height, image_width = image.shape

    # down size to number of dots
    if image_height == max(image_height,image_width):
        downsized_image = cv2.resize(image,(int(image_height*(max_dots/image_width)),max_dots))
    else:
        downsized_image = cv2.resize(image,(max_dots,int(image_height*(max_dots/image_width))))

    # extract dimensions of new image
    downsized_image_height, downsized_image_width = downsized_image.shape

    # set how big we want our final image to be
    multiplier = 100

    # set the size of our blank canvas
    blank_img_height = downsized_image_height * multiplier
    blank_img_width = downsized_image_width * multiplier

    # set the padding value so the dots start in frame (rather than being off the edge
    padding = int(multiplier/2)

    # create canvas containing just the background colour
    blank_image = np.full(((blank_img_height),(blank_img_width),3), background_color,dtype=np.uint8)

    # run through each pixel and draw the circle on our blank canvas
    bar = progressbar.ProgressBar(widgets=["Pop Art Image ", progressbar.Bar()])    
    for y in bar(range(0,downsized_image_height)):
        for x in range(0,downsized_image_width):
            cv2.circle(blank_image,(((x*multiplier)+padding),((y*multiplier)+padding)), int((0.6 * multiplier) * ((255-downsized_image[y][x])/255)), dot_color, -1)

    return blank_image
