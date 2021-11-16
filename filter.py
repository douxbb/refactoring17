from PIL import Image
import numpy as np


def set_color(arr, i, j, cell_size, brightness, graduation):
    value = int(brightness // graduation) * graduation
    arr[i: i + cell_size, j: j + cell_size] = value
    return arr


def get_avg_brightness(arr, i, j, cell_size):
    interval = arr[i: i + cell_size, j: j + cell_size]
    summa = np.sum(interval)
    result = int(summa // 3 // (cell_size ** 2))
    return result


def filter(arr, cell_size, graduation):
    width = len(arr)
    height = len(arr[1])
    for i in range(0, width - cell_size + 1, cell_size):
        for j in range(0, height - cell_size + 1, cell_size):
            brightness = get_avg_brightness(arr, i, j, cell_size)
            arr = set_color(arr, i, j, cell_size, brightness, graduation)
    return arr


img = Image.open("img2.jpg")
array = np.array(img)
array = filter(array, 10, 50)
res = Image.fromarray(array)
res.save('res.jpg')