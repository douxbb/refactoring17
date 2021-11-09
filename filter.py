from PIL import Image
import numpy as np

def get_image_brightness(rows, columns, img_array, mosaic_size) -> int:
    return sum((int(img_array[r_index][c_index][0]) 
            + int(img_array[r_index][c_index][1]) 
            + int(img_array[r_index][c_index][2])) // 3 
            for c_index in range(columns, columns + mosaic_size) 
            for r_index in range(rows, rows + mosaic_size))

def create_grayscale_img_bit(rows, columns, mosaic_size, brightness) -> None:
    for r_index in range(rows, rows + mosaic_size):
            for c_index in range(columns, columns + mosaic_size):
                img_array[r_index][c_index] = np.full(3, brightness)

img = Image.open("img2.jpg")
img_array = np.array(img)
rows_length = len(img_array) 
columns_length = len(img_array[0])
mosaic_size = 10
grayscale = 50

rows = 0
while rows < rows_length:
    columns = 0
    while columns < columns_length:
        create_grayscale_img_bit(rows, 
                                columns, 
                                mosaic_size, 
                                get_image_brightness(rows, 
                                                    columns, 
                                                    img_array, 
                                                    mosaic_size) // mosaic_size**2 // grayscale*grayscale)
        columns += mosaic_size
    rows += mosaic_size
Image.fromarray(img_array).save('res.jpg')
