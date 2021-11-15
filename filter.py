from PIL import Image
import numpy as np


def mosaic_to_gray(array_img: np.array, mosiac_size, step_grad):
    width = len(array_img)
    height = len(array_img[1])
    for x in range(0,width,mosiac_size):
        for y in range(0,height, mosiac_size):
            pixel_mosaic = array_img[x:x+mosiac_size,y:y+mosiac_size]
            medium_color_mosaic = (np.sum(pixel_mosaic) / 3) // (mosiac_size * mosiac_size)
            for i in range(x, x + mosiac_size):
                for j in range(y, y + mosiac_size):
                    array_img[i][j].fill((medium_color_mosaic // (step_grad*10))*(step_grad*10))
    return array_img


img_name = input("Введите название файла для изменения: ")
result_name = input("Введите название результирующего файла: ")
square_size = int(input("Введите размер мозаики: "))
gradation = int(input("Введите уровень градации серого: "))
Image.fromarray(mosaic_to_gray(np.array(Image.open(img_name)), square_size, gradation)).save(result_name)
print("Мозаика готова!")
