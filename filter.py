from PIL import Image
import numpy as np


def refactor_pixels(pixels, i, j, step, pixel_size):
    middle_brightness = int(int(np.sum(pixels[i:i + pixel_size, j:j + pixel_size])) // 3 // (pixel_size ** 2))
    pixels[i: i + pixel_size, j: j + pixel_size] = int(middle_brightness // step) * step

def pixelation(pixels, step, pixel_size):
    width = len(pixels)
    height = len(pixels[1])
    pixels = pixels[:width // pixel_size * pixel_size, :height // pixel_size * pixel_size]
    width = len(pixels)
    height = len(pixels[1])
    for i in range(0, width - pixel_size + 1, pixel_size):
        for j in range(0, height - pixel_size + 1, pixel_size):
            refactor_pixels(pixels, i, j, step, pixel_size)
    return pixels

img = Image.open("img2.jpg")
pixels = np.array(img)
res = Image.fromarray(pixelation(pixels, 50, 20))
res.save('res.jpg')

