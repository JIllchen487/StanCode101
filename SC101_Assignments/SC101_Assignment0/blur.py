"""
File: blur.py
Name:
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage
BLUR_INDEX = 5

def main():
    """
    TODO: put in a picture and show the blurred version of it
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)

    for i in range(BLUR_INDEX):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img: An image to be blurred
    :return: a blurred image
    """
    new_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            pixel = new_img.get_pixel(x, y)
            sum_red = 0
            sum_blue = 0
            sum_green = 0
            if x == 0:
                if y == 0:
                    for i in range(0, 2):
                        for j in range(0, 2):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 4
                    pixel.blue = sum_blue / 4
                    pixel.green = sum_green / 4
                elif y == img.height-1:
                    for i in range(0, 2):
                        for j in range(-1, 1):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 4
                    pixel.blue = sum_blue / 4
                    pixel.green = sum_green / 4
                else:
                    for i in range(0, 2):
                        for j in range(-1, 2):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 6
                    pixel.blue = sum_blue / 6
                    pixel.green = sum_green / 6
            elif y == 0:
                if x == img.width-1:
                    for i in range(-1, 1):
                        for j in range(0, 2):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 4
                    pixel.blue = sum_blue / 4
                    pixel.green = sum_green / 4
                else:
                    for i in range(-1, 2):
                        for j in range(0, 2):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 6
                    pixel.blue = sum_blue / 6
                    pixel.green = sum_green / 6
            elif x == img.width-1:
                if y == img.height-1:
                    for i in range(-1, 1):
                        for j in range(-1, 1):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 4
                    pixel.blue = sum_blue / 4
                    pixel.green = sum_green / 4
                else:
                    for i in range(-1, 1):
                        for j in range(-1, 2):
                            neighbor = img.get_pixel(x + i, y + j)
                            sum_red += neighbor.red
                            sum_blue += neighbor.blue
                            sum_green += neighbor.green
                    pixel.red = sum_red / 6
                    pixel.blue = sum_blue / 6
                    pixel.green = sum_green / 6
            elif y == img.height-1:
                for i in range(-1, 2):
                    for j in range(-1, 1):
                        neighbor = img.get_pixel(x + i, y + j)
                        sum_red += neighbor.red
                        sum_blue += neighbor.blue
                        sum_green += neighbor.green
                pixel.red = sum_red / 6
                pixel.blue = sum_blue / 6
                pixel.green = sum_green / 6
            else:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        neighbor = img.get_pixel(x+i, y+j)
                        sum_red += neighbor.red
                        sum_blue += neighbor.blue
                        sum_green += neighbor.green

                pixel.red = sum_red/9
                pixel.blue = sum_blue/9
                pixel.green = sum_green/9
    return new_img


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
