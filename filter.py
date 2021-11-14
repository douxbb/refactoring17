from PIL import Image
import numpy as np


def find_brightness(i, j, arr, m_h, m_w):
    count = np.sum(arr[i: i + m_h, j: j + m_w]) / 3
    count = count // (m_h * m_w)
    return count


def make_mosaic(arr, m_h, m_w, grad):
    height = len(arr)
    width = len(arr[1])
    i = 0
    while i < height:
        j = 0
        while j < width:
            brightness = find_brightness(i, j, arr, m_h, m_w)
            arr[i: i + m_h, j: j + m_w, :] = int(brightness // grad) * grad
            j = j + m_w
        i = i + m_h


images = input('Введите имя исходного файла и нового(через запятую): ').split(',')
arr_img = np.array(Image.open(images[0] + ".jpg"))
size_h, size_w = input('Введите размер мозаики(через запятую): ').split(',')
num_grad = int(input('Введите число градации: '))
make_mosaic(arr_img, int(size_h), int(size_w), num_grad)
res = Image.fromarray(arr_img)
res.save(images[1] + ".jpg")
