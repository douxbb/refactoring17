from PIL import Image

import numpy as np


class PixelArt:
    def __init__(self, chunk_size, color_step):
        self.chunk_size = chunk_size
        self.color_step = color_step
        self.result = None

    def generate_art(self):
        image = Image.open("img2.jpg")
        array = np.array(image)
        self.result = np.array(image)
        x_len = len(array)
        y_len = len(array[1])
        x = 0
        while x < x_len:
            y = 0
            while y < y_len:
                chunk_color = 0
                for n in range(x, x + (self.chunk_size if x_len - x >= self.chunk_size else x_len - x)):
                    for n1 in range(y, y + (self.chunk_size if y_len - y >= self.chunk_size else y_len - y)):
                        chunk_color += sum(map(int, array[n][n1])) / 3
                chunk_color = int(chunk_color // 100)
                for n in range(x, x + (self.chunk_size if x_len - x >= self.chunk_size else x_len - x)):
                    for n1 in range(y, y + (self.chunk_size if y_len - y >= self.chunk_size else y_len - y)):
                        self.result[n][n1] = [(chunk_color // self.color_step) * self.color_step for _ in range(3)]
                y += self.chunk_size
            x += self.chunk_size

    def save(self):
        result = Image.fromarray(self.result)
        result.save('res.jpg')


if __name__ == '__main__':
    art = PixelArt(int(input('Enter chunk size: ')), 255 // int(input('Enter count of colors: ')))
    art.generate_art()
    art.save()
