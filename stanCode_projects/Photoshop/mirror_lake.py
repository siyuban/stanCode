"""
File: mirror_lake.py
Name: 萬思妤
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image.
    :return: The image that creates a mirror lake vibe by placing an inverse
            image of mt-rainier.jpg below the original one.
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            old_pixel = img.get_pixel(x, y)
            new_pixel1 = blank_img.get_pixel(x, y)
            new_pixel2 = blank_img.get_pixel(x, blank_img.height-1-y)

            new_pixel1.red = old_pixel.red
            new_pixel1.green = old_pixel.green
            new_pixel1.blue = old_pixel.blue

            new_pixel2.red = old_pixel.red
            new_pixel2.green = old_pixel.green
            new_pixel2.blue = old_pixel.blue
    return blank_img


def main():
    """
    Make a new image that creates a mirror lake vibe by placing an inverse image of
    mt-rainier.jpg below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
