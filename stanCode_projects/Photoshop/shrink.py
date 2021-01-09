"""
File: shrink.py
Name: 萬思妤
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage, a new image half the width and height of the original.
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width//2, img.height//2)
    for x in range(new_img.width):
        for y in range(new_img.height):
            old_pixel = img.get_pixel(2*x, 2*y)
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = old_pixel.red
            new_pixel.blue = old_pixel.blue
            new_pixel.green = old_pixel.green
    return new_img


def main():
    """
    Create a new image half the width and height of the original.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
