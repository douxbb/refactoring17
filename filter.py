from PIL import Image
import numpy as np
class ConvertImage:

    def __init__(self, image, size, step):
        self.image = image
        self.size = size
        self.step = 255 // step

    def convert_image(self):
        height = len(self.image)
        width = len(self.image[1])
        for i in range(0, height, self.size):
            for j in range(0, width, self.size):
                medium_brightness = self.get_medium_brightness(i, j)
                self.set_grayscale(medium_brightness, i, j)
        return Image.fromarray(self.image)

    def set_grayscale(self, medium_brightness, i, j):
        for x in range(i, i + self.size):
            for y in range(j, j + self.size):
                self.image[x][y][0] = int(medium_brightness // self.step) * self.step / 3
                self.image[x][y][1] = int(medium_brightness // self.step) * self.step / 3
                self.image[x][y][2] = int(medium_brightness // self.step) * self.step / 3

    def get_medium_brightness(self, i, j):
        medium_brightness = 0
        for x in range(i, i + self.size):
            for y in range(j, j + self.size):
                pixel = self.image[x][y]
                pixel_sum = pixel.sum()
                medium_brightness += pixel_sum
        medium_brightness = int(medium_brightness // self.size ** 2)
        return medium_brightness


original_image = Image.open("img2.jpg")
pixels = np.array(original_image)
result = ConvertImage(pixels, 10, 50).convert_image()
result.save('res.jpg')
