from PIL import Image
import numpy as np


def get_mosaic_image(image, mosaic_size=10, gradation=4):
    threshold = 255 // gradation
    image_tensor = np.array(image).astype(int)
    image_length = len(image_tensor)
    image_height = len(image_tensor[0])
    i = 0
    while i < image_length:
        j = 0
        while j < image_height:
            colors_sum = get_matrix_elem_sum(image_tensor, mosaic_size, i, j)
            average_color = int(colors_sum // (mosaic_size ** 2))
            set_color(int(average_color // threshold) * threshold / 3, image_tensor, mosaic_size, i, j)
            j += mosaic_size
        i += mosaic_size
    return Image.fromarray(np.uint8(image_tensor))


def get_matrix_elem_sum(m, mosaic_size, i, j):
    color_sum = 0
    for sector_i in range(i, i + mosaic_size):
        for sector_j in range(j, j + mosaic_size):
            n1 = m[sector_i][sector_j][0]
            n2 = m[sector_i][sector_j][1]
            n3 = m[sector_i][sector_j][2]
            M = n1 + n2 + n3
            color_sum += M
    return color_sum


def set_color(new_color, tensor, mosaic_size, i, j):
    for sector_i in range(i, i + mosaic_size):
        for sector_j in range(j, j + mosaic_size):
            for c in range(3):
                tensor[sector_i][sector_j][c] = new_color


source_img = Image.open("img2.jpg")
res = get_mosaic_image(source_img, mosaic_size=15, gradation=5)
res.save('res.jpg')
