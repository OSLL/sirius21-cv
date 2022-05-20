# python 3.8
# Занятие 2. Морфологические преобразования

import cv2 as cv
import numpy  # noqa: F401
import os

color_limits_ranges = [(0, 0, 0), (359, 100, 100), (0, 0, 0), (179, 255, 255)]

colors = {1: "Красный",
          2: "Оранжевый", 3: "Светло-оранжевый",
          4: "Жёлтый",
          5: "Зелёный",
          6: "Синий", 7: "Голубой", 8: "Бирюзовый",
          9: "Фиолетовый"}
color_limits = {1: [((1, 30, 0), (8, 100, 100)), ((357, 30, 0), (359, 100, 100))],
                2: [((22, 50, 10), (33, 100, 100))],
                3: [((37, 60, 10), (43, 100, 100))],
                4: [((53, 45, 10), (58, 100, 100))],
                5: [((105, 10, 10), (115, 100, 100))],
                6: [((255, 20, 20), (266, 100, 100))],
                7: [((212, 20, 20), (221, 100, 100))],
                8: [((187, 30, 20), (196, 100, 100))],
                9: [((279, 40, 30), (287, 100, 100))]}


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
    color_limits_255 = {col: [tuple(tuple(map(convert_range, c, *color_limits_ranges)) for c in cl)
                              for cl in color_limits[col]]
                        for col in color_limits}

    image_path = os.path.normpath(input("Введите путь к изображению(он не должен содержать русские буквы): "))
    if checkFile(image_path) is False:
        print("Ошибка. Такого файла не существует. ")
        return

    for n in colors:
        print(f"{n} - {colors[n]}")
    color = int(input("Введите номер цвета: "))
    if color not in colors:
        print("Ошибка. Неправильный цвет. ")
        return

    color_limit = color_limits_255[color]

    img = cv.imread(image_path)
    img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    if len(color_limit) == 1:
        mask = cv.inRange(img_hsv, *color_limit[0])
    elif len(color_limit) == 2:
        mask0 = cv.inRange(img_hsv, *color_limit[0])
        mask1 = cv.inRange(img_hsv, *color_limit[1])
        mask = cv.bitwise_or(mask0, mask1)
        del mask0, mask1
    else:
        raise ValueError

    kernel = numpy.ones((5, 5))
    mask = cv.dilate(mask, kernel)
    mask = cv.erode(mask, kernel)
    mask = cv.dilate(mask, kernel)

    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    quantity = len(hierarchy[0]) if hierarchy is not None else 0

    rects = []
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        rects.append([(x, y), (w, h)])

    coords = []
    sizes = []
    for rect in rects:
        x, y, w, h = rect[0][0], rect[0][1], rect[1][0], rect[1][1]
        coords.append((round(x + w / 2), round(y + h / 2)))
        sizes.append(int(numpy.mean((w, h))))

    minDistance = -1
    minD_x0, minD_y0 = -1, -1
    minD_x1, minD_y1 = -1, -1
    for c0 in coords:
        for c1 in coords:
            if c0 != c1:
                x0, y0 = c0[0], c0[1]
                x1, y1 = c1[0], c1[1]
                distance = round(numpy.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2))
                if distance < minDistance or minDistance == -1:
                    minDistance = distance
                    minD_x0, minD_x1 = x0, x1
                    minD_y0, minD_y1 = y0, y1

    if minDistance != -1:
        cv.line(img, (minD_x0, minD_y0), (minD_x1, minD_y1), (255, 0, 255), 2)

    print(f"Цвет: {colors[color]}. ")
    print(f"Количество мячиков этого цвета на картинке: {quantity}. " if quantity != 0 else
          "На изображении нет мячиков этого цвета. ")
    for b in range(quantity):
        c = coords[b]
        s = sizes[b]
        x, y = c[0], c[1]
        print(f"{b+1}. x: {x}, y: {y}, diameter: {s}")
    if minDistance != -1:
        print(f"Минимальное расстояние: {minDistance}")

    cv.imshow("image", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
