from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                n1 = arr[n][m][0]
                n2 = arr[n][m][1]
                n3 = arr[n][m][2]
                M = int(n1) + int(n2) + int(n3)
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for m in range(j, j + 10):
                arr[n][m][0] = int(s // 50) * 50 / 3
                arr[n][m][1] = int(s // 50) * 50 / 3
                arr[n][m][2] = int(s // 50) * 50 / 3
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('res.jpg')
