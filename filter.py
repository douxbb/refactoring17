from argparse import ArgumentParser, Namespace
from typing import Tuple

import numpy as np
from PIL import Image


class ValidationError(Exception):
    pass


def _save_image(image_array: np.ndarray, output_image_path: str) -> None:
    """
    Сохранить изображение по указанному пути
    """
    res = Image.fromarray(image_array)
    res.save(output_image_path)


def _load_image(input_image_path: str) -> np.ndarray:
    """
    Загрузить изображение по указанному пути
    """
    img = Image.open(input_image_path)
    return np.array(img, dtype=np.uint8)


def _get_and_validate_size(pixel_matrix: np.ndarray, segment_size: int) -> Tuple[int, int]:
    """
    Получение и валидация размеров матрицы пикселей
    """
    rows_count = len(pixel_matrix)

    if not rows_count:
        raise ValidationError('Изображение пустое')

    columns_count = len(pixel_matrix[0])

    if rows_count % segment_size != 0 or columns_count % segment_size != 0:
        raise ValidationError(
            f"Невозможно разделить изображение размером: ({rows_count}, "
            "{columns_count}) на сегменты размером: {segment_size}"
        )
    
    return rows_count, columns_count


def _calculate_mean_by_sector(pixel_matrix: np.ndarray, begin_corrdinates: Tuple[int, int], segment_size: int) -> int:
    min_row_number, min_column_number = begin_corrdinates
    mean_mosaic_segment_value = 0

    for current_row_number in range(
        min_row_number, min_row_number + segment_size
    ):
        for current_column_number in range(
            min_column_number, min_column_number + segment_size
        ):

            red, green, blue = pixel_matrix[current_row_number][
                current_column_number
            ]
            mean_rgb_value = (int(red) + int(green) + int(blue)) // 3
            mean_mosaic_segment_value += mean_rgb_value

    return int(
        mean_mosaic_segment_value // (segment_size ** 2)
    )


def _calculate_grayscale_gradation(mean_mosaic_segment_value: int, grayscale_gradation: int) -> int:
    return int(mean_mosaic_segment_value // grayscale_gradation) * grayscale_gradation


def _insert_grayscale_segment(pixel_matrix: np.ndarray, begin_corrdinates: Tuple[int, int], segment_size: int, grayscale_gradation_value: int) -> None:
    min_row_number, min_column_number = begin_corrdinates
    for current_row_number in range(
        min_row_number, min_row_number + segment_size
    ):
        for current_column_number in range(
            min_column_number, min_column_number + segment_size
        ):
            pixel_matrix[current_row_number][current_column_number][...] = grayscale_gradation_value

def _create_pixel_art(
    input_image_path: str,
    output_image_path: str,
    segment_size: int = 10,
    grayscale_gradation: int = 50,
) -> None:
    pixel_matrix = _load_image(input_image_path)

    rows_count, columns_count = _get_and_validate_size(pixel_matrix, segment_size)

    min_row_number = 0

    while min_row_number < rows_count:
        min_column_number = 0

        while min_column_number < columns_count:
            mean_mosaic_segment_value = _calculate_mean_by_sector(pixel_matrix, (min_row_number, min_column_number), segment_size)
            grayscale_gradation_value = _calculate_grayscale_gradation(mean_mosaic_segment_value, grayscale_gradation)

            _insert_grayscale_segment(
                pixel_matrix, (min_row_number, min_column_number), segment_size, grayscale_gradation_value
            )

            min_column_number = min_column_number + segment_size
        min_row_number = min_row_number + segment_size

    _save_image(pixel_matrix, output_image_path)
 

def _parser() -> Namespace:
    parser = ArgumentParser(description="Преобразование изображения в пиксель арт")
    parser.add_argument(
        "-i",
        "--input-image",
        type=str,
        default="./docs/examples/img2.jpg",
        help="Путь до ихображения которое вы хотите преобразовать",
    )
    parser.add_argument(
        "-o",
        "--output-image",
        type=str,
        default="./docs/examples/res.jpg",
        help="Путь, куда вы хотите сохранить изображение",
    )
    parser.add_argument(
        "-s",
        "--segment-size",
        type=int,
        default=10,
        help="Размер сегмента мозаики",
    )
    parser.add_argument(
        "-g",
        "--grayscale-gradation",
        type=int,
        default=50,
        help="Градация серого цвета",
    )
    return parser.parse_args()


def main():
    args = _parser()
    _create_pixel_art(
        args.input_image, args.output_image, args.segment_size, args.grayscale_gradation
    )


if __name__ == "__main__":
    main()
