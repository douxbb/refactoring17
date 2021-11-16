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
        middle = 0
        for x in range(i, i + 10):
            for y in range(j, j + 10):
                r = int(arr[x][y][0])
                g = int(arr[x][y][1])
                b = int(arr[x][y][2])
                brightness = int(r + g + b)//3
                middle += brightness
        middle = int(middle // 100)
        for x in range(i, i + 10):
            for r in range(j, j + 10):
                arr[x][r][0] = int(middle // 50) * 50
                arr[x][r][1] = int(middle // 50) * 50
                arr[x][r][2] = int(middle // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
