from PIL import Image
import numpy as np
def set_color(arr, i, j, cell_size, brightness, graduation):
    for row in range(i, i + cell_size):
        for column in range(j, j + cell_size):
            value = int(brightness // graduation) * graduation
            arr[row][column][0] = value
            arr[row][column][1] = value
            arr[row][column][2] = value
    return arr


def get_avg_brightness(arr, i, j, cell_size):
    result = 0
    for row in range(i, i + cell_size):
        for column in range(j, j + cell_size):
            r = arr[row][column][0]
            g = arr[row][column][1]
            b = arr[row][column][2]
            sum = int(r) + int(g) + int(b)
            result += sum
    result = int(result // 3 // (cell_size ** 2))
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