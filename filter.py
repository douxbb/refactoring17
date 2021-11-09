from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
#обрезает лишнее кол-во пикселей
while len(arr) % 10 != 0: arr = np.delete(arr, len(arr) // 10 * 10, 0)
while len(arr[0]) % 10 != 0: arr = np.delete(arr, len(arr[0]) // 10 * 10, 1)
#
a = len(arr)
a1 = len(arr[0])
i = 0
while i < a - 9:
    j = 0
    while j < a1 - 9:
        s = 0
        for r_index in range(i, i + 10):
            for c_index in range(j, j + 10):
                r = arr[r_index][c_index][0]
                g = arr[r_index][c_index][1]
                b = arr[r_index][c_index][2]
                M = int(r) + int(g) + int(b)
                s += M
        s = s // 100
        for r_index in range(i, i + 10):
            for c_index in range(j, j + 10):
                arr[r_index][c_index][0] = s // 50 * 50 // 3
                arr[r_index][c_index][1] = s // 50 * 50 // 3
                arr[r_index][c_index][2] = s // 50 * 50 // 3
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')