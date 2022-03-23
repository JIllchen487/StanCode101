"""
File: stanCodoshop.py
Name: 
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """
    red_dist = pixel.red - red
    green_dist = pixel.green - green
    blue_dist = pixel.blue - blue
    dist = (red_dist**2 + green_dist**2 + blue_dist**2)**(1/2)
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """
    sum_red = 0
    sum_green = 0
    sum_blue = 0
    n_pixels = 0
    for pixel in pixels:
        sum_red += pixel.red
        sum_green += pixel.green
        sum_blue += pixel.blue
        n_pixels += 1
    red = int(sum_red / n_pixels)
    green = int(sum_green / n_pixels)
    blue = int(sum_blue / n_pixels)
    return [red, green, blue]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    avg_rgb = get_average(pixels)
    # print('avg_rgb:', avg_rgb)
    shortest_dist = (255**2 + 255**2 + 255**2)**(1/2)
    closest_pixel = pixels[0]
    for pixel in pixels:
        # print('pixel_rgb=', pixel.red, pixel.green, pixel.blue)
        dist = get_pixel_dist(pixel, avg_rgb[0], avg_rgb[1], avg_rgb[2])
        # print(dist)
        if dist < shortest_dist:
            # print('shortest dist=')
            shortest_dist = dist
            closest_pixel = pixel
            # print('closest_pixel rgb=', closest_pixel.red, closest_pixel.green, closest_pixel.blue)
    return closest_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #
    # Write code to populate image and create the 'ghost' effect
    for i in range(width):
        for j in range(height):
            pixels = []
            for image in images:
                pixel = image.get_pixel(i, j)
                pixels.append(pixel)
            chosen_px = get_best_pixel(pixels)
            result.get_pixel(i, j).red = chosen_px.red
            result.get_pixel(i, j).green = chosen_px.green
            result.get_pixel(i, j).blue = chosen_px.blue

    # print(get_pixel_dist(green_pixel, 5, 255, 10))
    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
