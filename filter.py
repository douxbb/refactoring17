from PIL import Image
import numpy as np

def scale_middle_brightness(arr, i, j, pixel_size, width, height):
    middle_brightness = 0
    for n in range(i, i + pixel_size):
        if n >= width:
            break
        for n1 in range(j, j + pixel_size):
            if n1 >= height:
                break
            r = int(arr[n][n1][0])
            g = int(arr[n][n1][1])
            b = int(arr[n][n1][2])
            brightness = int(r + g + b) // 3
            middle_brightness += brightness
    return int(middle_brightness // (pixel_size ** 2))

def refactor_pixels(arr, i, j, middle_brightness, step, pixel_size, width, height):
    for n in range(i, i + pixel_size):
        if n >= width:
            break
        for n1 in range(j, j + pixel_size):
            if n1 >= height:
                break
            arr[n][n1][0] = int(middle_brightness // step) * step
            arr[n][n1][1] = int(middle_brightness // step) * step
            arr[n][n1][2] = int(middle_brightness // step) * step

def pixelation(arr, step, pixel_size):
    width = len(arr)
    height = len(arr[1])
    i = 0
    while i < width:
        j = 0
        while j < height:
            middle_brightness = scale_middle_brightness(arr, i, j, pixel_size, width, height)
            refactor_pixels(arr, i, j, middle_brightness, step, pixel_size, width, height)
            j = j + pixel_size
        i = i + pixel_size

img = Image.open("img2.jpg")
arr = np.array(img)

pixelation(arr, 50, 12)

res = Image.fromarray(arr)
res.save('res.jpg')
