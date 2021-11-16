from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
cell_size = 10;
step = 50;
for i in range(0, width - cell_size + 1, cell_size):
    for j in range(0, height - cell_size + 1, cell_size):
        avg_brightness = 0
        for row in range(i, i + cell_size):
            for column in range(j, j + cell_size):
                r = arr[row][column][0]
                g = arr[row][column][1]
                b = arr[row][column][2]
                sum = int(r) + int(g) + int(b)
                avg_brightness += sum
        avg_brightness = int(avg_brightness // 3 // (cell_size ** 2))
        for row in range(i, i + cell_size):
            for column in range(j, j + cell_size):
                arr[row][column][0] = int(avg_brightness // step) * step
                arr[row][column][1] = int(avg_brightness // step) * step
                arr[row][column][2] = int(avg_brightness // step) * step
res = Image.fromarray(arr)
res.save('res.jpg')