import cv2
import numpy as np

"""
downscale(IMAGE_PATH, WIDTH_PIXELS, HEIGHT_PIXELS): 
- takes an image file path and downscales it to the desired dimensions.
    https://learnopencv.com/image-resizing-with-opencv/
"""
def downscale(image_file, width, height):
    image = cv2.imread(image_file)
    cv2.imshow('Original Image', image)

    down_width = width
    down_height = height
    down_points = (down_width, down_height)
    resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

    cv2.imshow('Resized Down by defining height and width', resized_down)
    cv2.waitKey()

    cv2.destroyAllWindows()

def main():
    downscale('data/portra/R1-00178-001A.JPG',256,256)
    return

if __name__ == "__main__":
    main()