from PIL import Image
from PIL import ImageFilter
import sys, os
import random

def main(argv):
    # Check if arguments formed correctly
    if len(argv) < 2:
        sys.stderr.write("Usage: %s <image_1> <image_2>\n" % (argv[0],))
        return 1

    if not os.path.exists(argv[1]):
        sys.stderr.write("ERROR: Image %r was not found!\n" % (argv[1],))
        return 1

    if not os.path.exists(argv[2]):
        sys.stderr.write("ERROR: Image %r was not found!\n" % (argv[2],))
        return 1

    # Load the images
    image_1 = Image.open(argv[1])
    image_2 = Image.open(argv[2])
    
    # Resize image to smallest image size if necessary
    if (image_1.size) != (image_2.size):
        if image_1.size > image_2.size:
            image_1 = image_1.resize(image_2.size)
        else:
            image_2 = image_2.resize(image_1.size)

    # Mashup the images
    width, height = image_1.size
    for x in range(width):
        for y in range(height):
            # Use the average of each image's pixels
            pixel_1 = image_1.getpixel((x,y))
            pixel_2 = image_2.getpixel((x,y))
            average_pixel = ((pixel_1[0] + pixel_2[0])/2,(pixel_1[1] + pixel_2[1])/2,(pixel_1[2] + pixel_2[2])/2)
            image_1.putpixel((x,y), average_pixel)

    # Save the result
    image_1.save("result.png")

if __name__ == "__main__":
    sys.exit(main(sys.argv))
