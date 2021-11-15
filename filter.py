from PIL import Image
import numpy as np


def mosaic_to_gray(array_img: np.array, mosiac_size, step_grad):
    width = len(array_img)
    height = len(array_img[1])
    x = 0
    while x < width:
        y = 0
        while y < height:
            medium_color_mosaic = 0
            for i in range(x, x + mosiac_size):
                for j in range(y, y + mosiac_size):
                    r = int(array_img[i][j][0])
                    g = int(array_img[i][j][1])
                    b = int(array_img[i][j][2])
                    medium_color_mosaic += (r + g + b) / 3
            medium_color_mosaic = int(medium_color_mosaic // (mosiac_size * mosiac_size))
            for i in range(x, x + mosiac_size):
                for j in range(y, y + mosiac_size):
                    array_img[i][j][0] = int(medium_color_mosaic // step_grad) * step_grad
                    array_img[i][j][1] = int(medium_color_mosaic // step_grad) * step_grad
                    array_img[i][j][2] = int(medium_color_mosaic // step_grad) * step_grad
            y = y + mosiac_size
        x = x + mosiac_size
    return array_img


square_size = 10
gradation = 5
Image.fromarray(mosaic_to_gray(np.array(Image.open("img2.jpg")), square_size, gradation)).save('res.jpg')

