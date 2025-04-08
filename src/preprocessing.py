import os
import cv2

DEBUG = False
"""
downscale(IMAGE_PATH, OUTPUT_PATH, WIDTH_PIXELS, HEIGHT_PIXELS): 
- takes an image file path and downscales it to the desired dimensions.
    https://learnopencv.com/image-resizing-with-opencv/
"""
def downscale(image_file, output_path, width, height):
    image = cv2.imread(image_file)
    if image is None:
        print(f"Failed opening image: {image_file}")
        return
    if DEBUG: cv2.imshow('Original Image', image)

    resized_down = cv2.resize(image, (width,height), interpolation= cv2.INTER_AREA)
    cv2.imwrite(output_path, resized_down)
    
    if DEBUG: 
        cv2.imshow('Resized Down by defining height and width', resized_down)
        cv2.waitKey()
        cv2.destroyAllWindows()
    return

def batch_process(input_dir, output_dir, width, height):
    print(f"== Processing Photos in {input_dir}, saving to {output_dir}.")
    os.makedirs(output_dir, exist_ok=True)
    for filename in [f for f in os.listdir(input_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]:
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        downscale(input_path, output_path, width, height)
        print(f"Processed: {output_path}")

def main():
    input_folder = "data/portra"
    output_folder = "data/portra_preprocessed"
    batch_process(input_folder, output_folder, 256, 256)
    return

if __name__ == "__main__":
    main()