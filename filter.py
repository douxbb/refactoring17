from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
width = len(arr)
height = len(arr[1])
i = 0
while i < width:
    j = 0
    while j < height:
        s = 0
        for n in range(i, i + 10):
            if n >= width:
                break
            for n1 in range(j, j + 10):
                if n1 >= height:
                    break
                r = int(arr[n][n1][0])
                g = int(arr[n][n1][1])
                b = int(arr[n][n1][2])
                M = int(r + g + b) // 3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50
                arr[n][n1][1] = int(s // 50) * 50
                arr[n][n1][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
