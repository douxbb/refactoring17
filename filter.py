from PIL import Image
import numpy as np

def open_and_crop(file_name:str, cells_size:int) -> np.ndarray:
    pix_array = np.array(Image.open(file_name))
    rows, columns = len(pix_array), len(pix_array[0])
    pix_array = np.delete(pix_array, slice(rows // cells_size * cells_size - 1, rows - 1), 0)
    pix_array = np.delete(pix_array, slice(columns // cells_size * cells_size - 1, columns - 1), 1)
    return pix_array

def convert_to_mozaic(pixels_array:np.ndarray, cell_size:int, step_size:int):
    rows_amount = len(pixels_array)
    columns_amount = len(pixels_array[0])
    row_index = 0
    while row_index < rows_amount - (cell_size - 1):
        column_index = 0
        while column_index < columns_amount - (cell_size - 1):
            hue = 0
            for r_index in range(row_index, row_index + cell_size):
                for c_index in range(column_index, column_index + cell_size):
                    hue += (int(pixels_array[r_index][c_index][0]) 
                            + int(pixels_array[r_index][c_index][1]) 
                            + int(pixels_array[r_index][c_index][2])) // 3
            hue = hue // cell_size ** 2 // step_size * step_size
            for r_index in range(row_index, row_index + cell_size):
                for c_index in range(column_index, column_index + cell_size):
                    pixels_array[r_index][c_index] = np.full(3, hue)
            column_index += cell_size
        row_index += cell_size
    return pixels_array
cell = 10
step = 50
Image.fromarray(convert_to_mozaic(open_and_crop("img2.jpg", cell), cell, step)).save('res.jpg')