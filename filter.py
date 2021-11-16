import numpy as np
from PIL import Image


class PixelArt:
    def __init__(self, chunk_size, color_step, file_path, save_path):
        self.save_path = save_path
        self.file_path = file_path
        self.chunk_size = chunk_size
        self.color_step = color_step
        self.array = np.array(Image.open(file_path))

    def generate_art(self):
        x_len = len(self.array)
        y_len = len(self.array[1])
        for x in range(0, x_len, self.chunk_size):
            for y in range(0, y_len, self.chunk_size):
                chunk_size_x = self.chunk_size if x_len - x >= self.chunk_size else x_len - x
                chunk_size_y = self.chunk_size if y_len - y >= self.chunk_size else y_len - y
                chunk = self.get_chuck_color(x, y, chunk_size_x, chunk_size_y)
                for m in range(x, x + chunk_size_x):
                    for m1 in range(y, y + chunk_size_y):
                        self.array[m][m1] = chunk
        return self

    def get_chuck_color(self, x, y, chunk_size_x, chunk_size_y):
        color = (np.sum(self.array[x: x + chunk_size_x, y: y + chunk_size_y]) / 3 / self.chunk_size ** 2)
        return color - color % (255 / self.color_step)

    def save(self):
        Image.fromarray(self.array).save(self.save_path)


if __name__ == '__main__':
    PixelArt(int(input('Enter chunk size: ')),
             int(input('Enter count of colors: ')),
             input('Enter original file path: '),
             input('Enter result file path: ')).generate_art().save()
