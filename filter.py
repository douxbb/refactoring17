from argparse import ArgumentParser, Namespace

import numpy as np
from PIL import Image


def _create_pixel_art(input_image_path: str, output_image_path: str) -> None:
    img = Image.open(input_image_path)
    arr = np.array(img, dtype=np.uint8)
    a = len(arr)
    a1 = len(arr[0])
    i = 0

    while i < a - 9:
        j = 0
        while j < a1 - 9:
            s = 0
            for n in range(i, i + 10):
                for n1 in range(j, j + 10):
                    red, green, blue = arr[n][n1]
                    M = int(red) + int(green) + int(blue)
                    s += M
            s = int(s // 300)
            for n in range(i, i + 10):
                for n1 in range(j, j + 10):
                    arr[n][n1][0] = int(s // 50) * 50
                    arr[n][n1][1] = int(s // 50) * 50
                    arr[n][n1][2] = int(s // 50) * 50
            j = j + 10
        i = i + 10
    print(arr.dtype)
    res = Image.fromarray(arr)
    res.save(output_image_path)


def _parser() -> Namespace:
    parser = ArgumentParser(description='Преобразование изображения в пиксель арт')
    parser.add_argument('-i', '--input-image', default="./docs/examples/img2.jpg", help='Путь до ихображения которое вы хотите преобразовать')
    parser.add_argument('-o', '--output-image', default='./docs/examples/res.jpg', help='Путь, куда вы хотите сохранить изображение')
    return parser.parse_args()



def main():
    args = _parser()
    _create_pixel_art(args.input_image, args.output_image)


if __name__ == '__main__':
    main()
