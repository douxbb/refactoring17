from PIL import Image
import numpy as np

def open_and_crop(file_name:str, cells_size:int) -> np.ndarray:
    pix_array = np.array(Image.open(file_name))
    rows, columns = len(pix_array), len(pix_array[0])
    pix_array = np.delete(pix_array, slice(rows // cells_size * cells_size - 1, rows - 1), 0)
    pix_array = np.delete(pix_array, slice(columns // cells_size * cells_size - 1, columns - 1), 1)
    return pix_array

def convert_to_mozaic(file_name:str, cells_size:int, step_size:int) -> np.ndarray:
    pixels_array = open_and_crop(file_name, cells_size)
    rows_amount = len(pixels_array)
    columns_amount = len(pixels_array[0])
    row_index = 0
    while row_index < rows_amount - (cells_size - 1):
        column_index = 0
        while column_index < columns_amount - (cells_size - 1):
            hue = 0
            for r_index in range(row_index, row_index + cells_size):
                for c_index in range(column_index, column_index + cells_size):
                    hue += (int(pixels_array[r_index][c_index][0]) 
                            + int(pixels_array[r_index][c_index][1]) 
                            + int(pixels_array[r_index][c_index][2])) // 3
            hue = hue // cells_size ** 2 // step_size * step_size
            for r_index in range(row_index, row_index + cells_size):
                for c_index in range(column_index, column_index + cells_size):
                    pixels_array[r_index][c_index] = np.full(3, hue)
            column_index += cells_size
        row_index += cells_size
    return pixels_array
Image.fromarray(convert_to_mozaic(input("Введите имя файла: \n"), 
                                  int(input("Введите размер мозаики (в пикселах): \n")), 
                                  int(input("Введите размер шага оттенков: \n")))).save('res.jpg')