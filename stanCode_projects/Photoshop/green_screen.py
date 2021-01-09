"""
File: green_screen.py
Name:萬思妤
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, the background image.
    :param figure_img: SimpleImage, green screen figure image
    :return: SimpleImage, figure image with the green screen pixels replaced by pixels of background.
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            figure_pixel = figure_img.get_pixel(x, y)
            bigger = max(figure_pixel.red, figure_pixel.blue)
            if figure_pixel.green > bigger*2:
                background_img_pixel = background_img.get_pixel(x, y)
                figure_pixel.red = background_img_pixel.red
                figure_pixel.blue = background_img_pixel.blue
                figure_pixel.green = background_img_pixel.green
    return figure_img


def main():
    """
    Create a new image that uses MillenniumFalcon.png as background and replace the green
    pixels in "ReyGreenScreen.png".
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    space_ship.make_as_big_as(figure)
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
