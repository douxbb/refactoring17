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
            sector = image_tensor[i: i + mosaic_size, j: j + mosaic_size]
            colors_sum = np.sum(sector)
            average_color = int(colors_sum // (mosaic_size ** 2))
            set_color(int(average_color // threshold) * threshold / 3, image_tensor, mosaic_size, i, j)
            j += mosaic_size
        i += mosaic_size
    return Image.fromarray(np.uint8(image_tensor))

def set_color(new_color, tensor, mosaic_size, i, j):
    for sector_i in range(i, i + mosaic_size):
        for sector_j in range(j, j + mosaic_size):
            for c in range(3):
                tensor[sector_i][sector_j][c] = new_color


source_img = Image.open("img2.jpg")
res = get_mosaic_image(source_img, mosaic_size=15, gradation=5)
res.save('res.jpg')
