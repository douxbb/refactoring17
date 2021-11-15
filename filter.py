from PIL import Image
import numpy as np

def make_mosaic(array, grayscale:int, size_mosaic:int, row_length:int, column_length:int):
    array = array[0: row_length // size_mosaic * size_mosaic, 0: column_length // size_mosaic * size_mosaic]
    row_index = 0
    while row_index < row_length - (size_mosaic - 1):
        column_index = 0
        while column_index < column_length - (size_mosaic - 1):
            color = 0
            for step_row in range(row_index, row_index + size_mosaic):
                color += sum(map(lambda step_column: sum(map(int, array[step_row][step_column])) // 3,
                        range(column_index, column_index + size_mosaic)))
            color = ((color // size_mosaic**2) // grayscale) * grayscale
            for step_row in range(row_index, row_index + size_mosaic):
                for step_column in range(column_index, column_index + size_mosaic):
                    array[step_row][step_column] = np.full(3, color)
            column_index += size_mosaic
        row_index += size_mosaic
    return array

img_array = np.array(Image.open(input("Полное имя файла:  ")))
Image.fromarray(make_mosaic(img_array, int(input("Градации серого:  ")), 
                                    int(input("Размер мозайки:  ")), len(img_array),
                                    len(img_array[1]))).save('res.jpg')
