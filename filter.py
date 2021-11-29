from PIL import Image
import numpy as np
def get_pixel(i, j):
    sum = 0
    for n in range(i, i + pxSize):
        for m in range(j, j + pxSize):
            r = arr[n][m][0]
            g = arr[n][m][1]
            b = arr[n][m][2]
            sum += (int(r) + int(g) + int(b)) / 3
    return int(sum // (pxSize*pxSize))


def set_grey_pixels(colorSum, i, j):
    for n in range(i, i + pxSize):
        for m in range(j, j + pxSize):
            arr[n][m][0] = int(colorSum // gradation) * gradation
            arr[n][m][1] = int(colorSum // gradation) * gradation
            arr[n][m][2] = int(colorSum // gradation) * gradation
img = Image.open("img2.jpg")
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
res.save('res.jpg')
