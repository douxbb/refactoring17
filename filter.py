from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
arr = np.array(img).astype(int)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a:
    j = 0
    while j < a1:
        s = 0
        for n in range(i, i + 10):
            for g in range(j, j + 10):
                n1 = arr[n][g][0]
                n2 = arr[n][g][1]
                n3 = arr[n][g][2]
                M = n1 + n2 + n3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for n1 in range(j, j + 10):
                arr[n][n1][0] = int(s // 50) * 50 / 3
                arr[n][n1][1] = int(s // 50) * 50 / 3
                arr[n][n1][2] = int(s // 50) * 50 / 3
        j = j + 10
    i = i + 10
res = Image.fromarray(np.uint8(arr))
res.save('res.jpg')
