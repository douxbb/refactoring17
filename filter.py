from PIL import Image
from numpy import *
import numpy as np
class GreyImage:
    def __init__(self, pix_array, pix_size=10, gradation=5):
        self.image = np.array(pix_array)
        self.size = pix_size
        self.gradation = 255 // gradation
        self.height = len(self.image)
        self.width = len(self.image[0])

    def get_grey_image(self):
        for px in range(0, self.width, self.size):
            for y in range(0, self.height, self.size):
                self.get_grey_color(color=self.get_middle_color(px, y), px=px, y=y)
        return Image.fromarray(self.image)

    def get_middle_color(self, px, y):
        color = 0
        for column in range(px, px + self.size):
            for row in range(y, y + self.size):
                color += sum([int(self.image[column][row][i]) for i in range(3)])
        return int(color / 3 // (self.size ** 2))

    def get_grey_color(self, color, px, y):
        for column in range(
            px, px + self.size):
            for row in range(y, y + self.size):
                self.image[column][row][0] = int(color // self.gradation) * self.gradation
                self.image[column][row][1] = int(color // self.gradation) * self.gradation
                self.image[column][row][2] = int(color // self.gradation) * self.gradation


orig_image = Image.open("img2.jpg")
result = GreyImage(pix_array=orig_image, pix_size=int(input()), gradation=int(input())).get_grey_image()
result.save('res.jpg')
