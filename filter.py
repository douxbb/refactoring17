import numpy as np
from PIL import Image


class PixelArt:
    def __init__(self, chunk_size, color_step):
        self.chunk_size = chunk_size
        self.color_step = color_step
        image = Image.open("img2.jpg")
        self.array = np.array(image)
        self.result = np.array(image)
        self.x_len = len(self.array)
        self.y_len = len(self.array[1])

    def generate_art(self):
        for x in range(0, self.x_len, self.chunk_size):
            for y in range(0, self.y_len, self.chunk_size):
                chunk_color = [(int(sum([sum([sum(map(int, self.array[n][n1])) / 3
                                              for n1 in range(y, y + (self.chunk_size
                                                                      if self.y_len - y >= self.chunk_size
                                                                      else self.y_len - y))])
                                         for n in range(x, x + (self.chunk_size
                                                                if self.x_len - x >= self.chunk_size
                                                                else self.x_len - x))]) // 100) // self.color_step)
                               * self.color_step for _ in range(3)]
                for m in range(x, x + (self.chunk_size if self.x_len - x >= self.chunk_size else self.x_len - x)):
                    for m1 in range(y, y + (self.chunk_size if self.y_len - y >= self.chunk_size else self.y_len - y)):
                        self.result[m][m1] = chunk_color

    def save(self):
        result = Image.fromarray(self.result)
        result.save('res.jpg')


if __name__ == '__main__':
    art = PixelArt(int(input('Enter chunk size: ')), 255 // int(input('Enter count of colors: ')))
    art.generate_art()
    art.save()
