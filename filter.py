from PIL import Image
import numpy as np

def get_image_brightness(rows, columns, img_array, mosaic_size) -> int:
    return int(np.sum(img_array[rows: rows + mosaic_size, columns: columns + mosaic_size]) // 3 // (mosaic_size ** 2))

def create_img_bit(rows, columns, mosaic_size, brightness, img_array) -> list:
    img_array[rows: rows + mosaic_size, columns: columns + mosaic_size] = np.full(3, brightness)
    return img_array

def create_image(img_array, rows_length, columns_length, mosaic_size, grayscale):
    for rows in range(0, rows_length, mosaic_size):
        for columns in range(0, columns_length, mosaic_size):
            create_img_bit(rows, columns, mosaic_size, get_image_brightness(rows, columns, img_array, mosaic_size) // grayscale*grayscale,
                    img_array)
    return img_array

img_array = np.array(Image.open(input('Введите имя изображения в директории: ') + ".jpg"))
Image.fromarray(create_image(img_array, 
            len(img_array), 
            len(img_array[0]), 
            int(input('Введите размер мозаики: ')), 
            int(input('Введите шаг оттенка: ')))).save('res.jpg')
