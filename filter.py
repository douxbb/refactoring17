from PIL import Image
import numpy as np

def mosaic_to_gray(array, mosiac_size, gradation):
    width = len(array)
    height = len(array[1])
    for x in range(0, width, mosiac_size):
        for y in range(0,height, mosiac_size):
            pixel = array[x:x + mosiac_size, y:y + mosiac_size]
            medium_color = (np.sum(pixel)/3) // (mosiac_size * mosiac_size)
            
            for i in range(x, x + mosiac_size):
                for j in range(y, y + mosiac_size):
                    array[i][j].fill((medium_color // (gradation*10))*(gradation*10))
    return array

img_name, result_name= input("Название изменяемого файла: "), input("Название результирующего файла: ")
mosiac_size, gradation = int(input("Размер мозаики: ")), int(input("Уровень градации: "))
Image.fromarray(mosaic_to_gray(np.array(Image.open(img_name)), mosiac_size, gradation)).save(result_name)