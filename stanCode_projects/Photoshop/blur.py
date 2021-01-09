"""
File: blur.py
Name: 萬思妤
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, the original image.
    :return: SimpleImage, blurred image.
    """
    blank_img = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            blank_pixel = blank_img.get_pixel(x, y)
            if (x, y) == (0, 0):
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x+1, y)
                pixel_3 = img.get_pixel(x, y+1)
                pixel_4 = img.get_pixel(x+1, y+1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red)//4
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
            elif(x, y) == (0, img.height-1):
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red) // 4
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
            elif(x, y) == (img.width-1, img.height-1):
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x - 1, y - 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red) // 4
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
            elif(x, y) == (img.width-1, 0):
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x - 1, y + 1)
                pixel_4 = img.get_pixel(x, y + 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red) // 4
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue) // 4
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green) // 4
            elif 1 < x < img.width-1 and y == 0:
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x - 1, y + 1)
                pixel_4 = img.get_pixel(x, y + 1)
                pixel_5 = img.get_pixel(x+1, y+1)
                pixel_6 = img.get_pixel(x + 1, y)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red +
                                   pixel_6.red) // 6
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue +
                                    pixel_6.blue) // 6
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green +
                                     pixel_6.green) // 6
            elif x == 0 and 0 < y < img.height-1:
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x + 1, y)
                pixel_5 = img.get_pixel(x + 1, y + 1)
                pixel_6 = img.get_pixel(x, y + 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red +
                                   pixel_6.red) // 6
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue +
                                    pixel_6.blue) // 6
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green +
                                     pixel_6.green) // 6
            elif 1 < x < img.width-1 and y == img.height-1:
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x - 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                pixel_6 = img.get_pixel(x + 1, y)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red +
                                   pixel_6.red) // 6
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue +
                                    pixel_6.blue) // 6
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green +
                                     pixel_6.green) // 6
            elif x == img.width - 1 and 0 < y < img.height-1:
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x - 1, y + 1)
                pixel_6 = img.get_pixel(x, y + 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red +
                                   pixel_6.red) // 6
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue +
                                    pixel_6.blue) // 6
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green +
                                     pixel_6.green) // 6
            elif 0 < x < img.width - 1 and 0 < y < img.height - 1:
                pixel_1 = img.get_pixel(x, y)
                pixel_2 = img.get_pixel(x, y - 1)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x - 1, y + 1)
                pixel_6 = img.get_pixel(x, y + 1)
                pixel_7 = img.get_pixel(x + 1, y + 1)
                pixel_8 = img.get_pixel(x + 1, y)
                pixel_9 = img.get_pixel(x + 1, y - 1)
                blank_pixel.red = (pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red + pixel_5.red +
                                   pixel_6.red + pixel_7.red + pixel_8.red + pixel_9.red) // 9
                blank_pixel.blue = (pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue + pixel_5.blue +
                                    pixel_6.blue + pixel_7.blue + pixel_8.blue + pixel_9.blue) // 9
                blank_pixel.green = (pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green + pixel_5.green +
                                     pixel_6.green + pixel_7.green + pixel_8.green + pixel_9.green) // 9
    return blank_img


def main():
    """
    Blur the image (smiley-face.png) for 5 times and 10 times.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()
    blurred_img = blur(old_img)
    for i in range(4):
        blurred_img = blur(blurred_img)
    blurred_img.show()
    # Blur 5 times
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()
    # Blur 10 times


if __name__ == '__main__':
    main()
