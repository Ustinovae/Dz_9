from PIL import Image
import numpy as np


def get_average_brightness_of_cell(cell, gray_step):
    """Returns the average brightness of the cell

    :param cell:
    :type int
    :param gray_step:
    :type int
    :return:
    :type int

    >>> get_average_brightness_of_cell(10, 50)
    0
    >>> get_average_brightness_of_cell(30, 20)
    20
    >>> get_average_brightness_of_cell(78, 14)
    70
    """
    average_value = int(np.average(cell) // gray_step) * gray_step
    return average_value


def convert_image(pixels: np.array, c_size: int, gray_step: int, w: int, h: int):
    """Converting image pixels to pixel graphics

    :param pixels:
    :type np.array()
    :param c_size:
    :type int
    :param gray_step:
    :type int
    :param w:
    :type int
    :param h:
    :type int
    :return:
    :type np.array()

    """
    for i in range(0, w - c_size + 1, c_size):
        for j in range(0, h - c_size + 1, c_size):
            cell = pixels[i:i + c_size, j:j + c_size]
            cell.fill(get_average_brightness_of_cell(cell, gray_step))
    return pixels


name_image = "dog.jpg"
cell_size = 10
gradation_step = 50

img = Image.open(name_image)
image_pixels = np.array(img)
width = len(image_pixels)
height = len(image_pixels)

result_image = convert_image(image_pixels, cell_size, gradation_step, width, height)
res = Image.fromarray(result_image)

name_result = "filter_with_filename_res.jpg"
res.save(name_result)
