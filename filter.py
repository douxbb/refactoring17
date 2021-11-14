from PIL import Image
import numpy as np

class ConvertImage:
    def __init__(self, image, size, gradation):
        self.image = image
        self.size = size
        self.step = 255 // gradation

    def convert_image(self):
        height = len(self.image)
        width = len(self.image[1])
        for i in range(0, height, self.size):
            for j in range(0, width, self.size):
                medium_brightness = self.get_medium_brightness(i, j)
                self.set_grayscale(medium_brightness, i, j)
        return Image.fromarray(self.image)
    def set_grayscale(self, medium_brightness, i, j):
        self.image[i:i + self.size, j:j + self.size] = int(medium_brightness // self.step) * self.step / 3
    def get_medium_brightness(self, i, j):
        return int((self.image[i:i + self.size, j:j + self.size].sum()) // self.size ** 2)
    original_image = Image.open(input("Введите имя исходного изображения:"))
pixels = np.array(original_image)
result = ConvertImage(pixels, size=10, gradation=50).convert_image()
result.save((input("Введите имя изображения, в которое запишется результат:")))
