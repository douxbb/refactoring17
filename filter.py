from PIL import Image
import numpy as np
def get_pixel(i, j):
    sum = np.sum(arr[i:i + pxSize, j: j + pxSize]) / 3
    return int(sum // (pxSize * pxSize))


def set_grey_pixels(colorSum, i, j):
    arr[i:i + pxSize, j:j + pxSize, 0] = int(colorSum // gradation) * gradation
    arr[i:i + pxSize, j:j + pxSize, 1] = int(colorSum // gradation) * gradation
    arr[i:i + pxSize, j:j + pxSize, 2] = int(colorSum // gradation) * gradation
def img2pixel(original, result):
    global arr
    global gradation
    global pxSize
    img = Image.open(original)
    arr = np.array(img)
    height = len(arr)
    width = len(arr[1])
    i = 0

    gradation = int(input('Введите градацию серого: '))
    pxSize = int(input('Введите размер мазайки: '))
    while i < height:
        j = 0
        while j < width:
            s = get_pixel(i, j)
            set_grey_pixels(s, i, j)
            j = j + pxSize
        i = i + pxSize
    res = Image.fromarray(arr)
    res.save(result)

img2pixel(input("Название оригинала: "), input("Название копии: "))