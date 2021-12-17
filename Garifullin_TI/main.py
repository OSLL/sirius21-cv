import cv2 as cv
import numpy as np


# In:
# znak.png
# new.png

def main():
    path = input()
    if not is_accessible(path):
        return -1
    gen = process_img(path)
    name = input()
    save_img(gen, name)


def save_img(gen, name):
    if name == "":
        name = "generated.png"
    cv.imwrite(name, gen)


def process_img(path):
    img = cv.imread(path)
    lower_range = np.array([100, 100, 100])
    upper_range = np.array([255, 255, 255])
    mask = cv.inRange(img, lower_range, upper_range)
    mask = cv.bitwise_not(mask)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(img, contours, -1, (0, 255, 0), 3)
    # cv.imshow('window', img)
    # cv.waitKey(0)
    # cv.destroyAllWindows()

    return img


def is_accessible(path, mode='r'):
    """
    Проверка, является ли файл или папка из `path`
    доступным для работы в предоставленным `mode` формате.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


if __name__ == "__main__":
    main()
