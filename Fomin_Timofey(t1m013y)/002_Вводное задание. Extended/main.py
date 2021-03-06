# python 3.8
# Вводное задание. Extended

import cv2 as cv
import numpy  # noqa: F401
import os


def checkFile(path: str) -> bool:
    return os.path.isfile(path)


def cvOpenImg(path: str) -> numpy.ndarray:
    return cv.imread(path)


def main():
    low, high = (140, 0, 0), (255, 255, 255)

    image_path = os.path.normpath(input("Введите путь к изображению(он не должен содержать русские буквы): "))
    if checkFile(image_path) is False:
        print("Такого файла не существует. ")
        return
    image_dir = os.path.dirname(image_path)
    image_basename = os.path.basename(image_path)
    image_name, image_extension = os.path.splitext(image_basename)

    save_path = input("Введите путь сохранения картинки: ")
    save_path = os.path.normpath(save_path) if bool(save_path) else fr"{image_dir}\{image_name}_mask{image_extension}"

    img = cvOpenImg(image_path)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    mask = cv.inRange(img_hsv, low, high)
    print(f"Цветовой диапазон HSV: {low}-{high}")
    img_mask = cv.bitwise_and(img, img, mask=mask)

    cv.imwrite(save_path, img_mask)
    print(f"Изображение сохранено в {save_path}")


if __name__ == '__main__':
    main()
    input("Press Enter to quit. \n")
    exit()
