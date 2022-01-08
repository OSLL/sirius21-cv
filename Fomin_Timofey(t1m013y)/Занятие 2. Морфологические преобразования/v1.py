# python 3.8
# Занятие 2. Морфологические преобразования

import cv2 as cv
import numpy  # noqa: F401
import os

color_limits_ranges = [(0, 0, 0), (359, 100, 100), (0, 0, 0), (179, 255, 255)]

color_limits = [((1, 30, 0), (8, 100, 100)), ((357, 30, 0), (359, 100, 100))]


def convert_range(value: int, old_min: int, old_max: int, new_min: int, new_max: int) -> int:
    if not(old_min < old_max and new_min <= new_max):
        raise ValueError
    OldRange = (old_max - old_min)
    NewRange = (new_max - new_min)
    NewValue = (((value - old_min) * NewRange) / OldRange) + new_min
    return round(NewValue)


def checkFile(path: str) -> bool:
    return os.path.isfile(path)


def main():
    color_limits_255 = [tuple(tuple(map(convert_range, c, *color_limits_ranges)) for c in cl) for cl in color_limits]

    image_path = os.path.normpath(input("Введите путь к изображению(он не должен содержать русские буквы): "))
    if checkFile(image_path) is False:
        print("Такого файла не существует. ")
        return

    img = cv.imread(image_path)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    if len(color_limits_255) == 1:
        mask = cv.inRange(img_hsv, *color_limits_255[0])
    elif len(color_limits_255) == 2:
        mask0 = cv.inRange(img_hsv, *color_limits_255[0])
        mask1 = cv.inRange(img_hsv, *color_limits_255[1])
        mask = cv.bitwise_or(mask0, mask1)
    else:
        raise ValueError
    del mask0, mask1

    kernel = numpy.ones((5, 5))
    mask = cv.dilate(mask, kernel)
    mask = cv.erode(mask, kernel)
    mask = cv.dilate(mask, kernel)

    contours, hierarchy = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (255, 0, 0))

    quantity = len([el for el in hierarchy[0] if el[3] == -1] if hierarchy is not None else [])

    print(f"Красных мячиков на картинке: {quantity}. " if quantity != 0 else "На изображении нет красных мячиков. ")


if __name__ == '__main__':
    main()
    input("Press Enter to quit. \n")
    exit()
