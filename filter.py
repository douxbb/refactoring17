from PIL import Image
import numpy as np


def get_mosaic(image, size, gradation):
    limit = 255 // gradation
    image_arr = np.array(image).astype(int)
    image_len = len(image_arr)
    image_h = len(image_arr[0])
    i = 0
    while i < image_len:
        j = 0
        while j < image_h:
            sum_c = get_sum(image_arr, size, i, j)
            avg = int(sum_c // (size ** 2))
            set_color(int(avg // limit) * limit / 3, image_arr, size, i, j)
            j += size
        i += size
    return Image.fromarray(np.uint8(image_arr))


def get_sum(array, size, i, j):
    middle_brightness = 0
    for x in range(i, i + size):
        for y in range(j, j + size):
            r = array[x][y][0]
            g = array[x][y][1]
            b = array[x][y][2]
            brightness = r + g + b
            middle_brightness += brightness
    return middle_brightness


def set_color(new_c, matrix, size, i, j):
    for x in range(i, i + size):
        for y in range(j, j + size):
            for z in range(3):
                matrix[x][y][z] = new_c


img = Image.open("img2.jpg")
res = get_mosaic(img, size=15, gradation=5)
res.save('res.jpg')